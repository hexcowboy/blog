Title: Making a Capture the Flag Machine
Date: 2021-06-26 20:30
Category: CTF
Tags: ctf, hackthebox, provinggrounds
Author: hexcowboy
Summary: Create a CTF-like box using bash scripts and make some money

This week I spent the majority of my time completing a machine for Offensive Security Proving Grounds. I figured this would be an easy task, but it ended up taking a lot more time than I had anticipated.

Offensive Security recently started accepting user submissions. Hack the Box also does this except with different criteria and pay grades. I recommend taking a look at both programs to see which platform you prefer to create for.

## Requirements

This is no easy task without some previous knowledge of system scripting and automation. At a *bare minimum*, I would recommend having the following skills:

- Bash scripting
- Basic networking
- Build automation

## Plan

This process was entirely new to me. I decided to jump right away into developing an exploit I had read about earlier this week involving [improper input validation in NPM](https://sick.codes/sick-2021-011).  I would need to develop an entirely custom application just to provide 1 attack vector. After about 4 hours I realized that developing an application and writing an exploit just for the sake of using it for a CTF box is **not a sustainable method**.

I decided to structure my plan a bit better, to spend my time more efficiently. After all, being paid $500 sounds nice until you work out your hourly wage to be less than $10.

Here is the attack vector structure I eventually came up with:

1. The attacker gains an initial foothold with a **pre-existing** public exploit
2. The attacker gains lateral privilege through a system misconfiguration
3. The attacker gains root privileges after exploiting a **pre-existing** public exploit

## Vector 1 - Public Authenticated Remote Exploit (and Default Credentials @solarwinds)

My most valuable resource for this phase was [Exploit Database](https://www.exploit-db.com/). I ended up choosing an exploit for a CRM application. The coolest thing about doing this is that I have *no idea* what a CRM is, but as long as it's vulnerable I can use it.

The CRM ended up having a public Docker image hosted on Docker Hub. The setup was extremely easy and I could set up the first vector just by creating a `docker-compose` file which was already provided by the application.

I decided to leave the default credentials and make that part of the first vector. The next part just involved the attacker executing the public exploit (which was an authenticated exploit), et voilà. First vector finished.

## Vector 2 - Container Breakout through misconfiguration

I decided to let the second vector play off of the first- find a way to exploit the Docker container.

I find Docker breakouts a bit cheesy because they are so popular in CTFs and are easily exploitable with tools like [botb](https://github.com/brompwnie/botb). Instead, I decided to make the breakout involve and improper mount.

Basically when a Docker container is run, you can provide a mount that shares files between the host operating system and the container. I made the Docker container mount **from** the host's `/home/user` folder **to** the application configuration.

I'm not entirely sure if anybody does this, but it's very probable since many system admins will create a user specifically for a Docker container.

This means that effectively the user can put their SSH key into the .ssh folder and get an SSH session as the user who started the container.

## Vector 3 - Privilege Escalation through a Linux bug

This was the most fun part of the process. I had read about the [polkit exploit](https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/) that has been present in Linux distros since around 2015. The problem with installing vulnerable software after it's patched is resolving dependencies for downgrading an old package.

For example, on Ubuntu 20.04, polkit was patched as version `ubuntu1.1`, where the vulnerable version is `ubuntu1`. The exploit also depended on `accountsservice` and `gnome-control-center` being installed.

When you downgrade one, the dependencies change for all. This caused a huge headache because I didn't know how to resolve all the dependencies to just downgrade `polkit`. I ended up finding a solution to this by installing `apt install aptitude` and running the install command like `aptitude install policykit-1=ubuntu1 accountsservice gnome-control-center` (or something similar, I can't remember the actual package names and version). This tools resolved all the dependencies and with that the final vector was complete.

## Adding Required Firewall Rules and Flags

The nice part about the Offensive Security program is that they provide you with a ZIP file that has an example build script. All I needed to do was copy some of the script and add it after my vectors. The code in question looks like this:

```bash
echo  "[+] Configuring firewall"
echo  "[+] Installing iptables"
echo  "iptables-persistent iptables-persistent/autosave_v4 boolean false" | debconf-set-selections
echo  "iptables-persistent iptables-persistent/autosave_v6 boolean false" | debconf-set-selections
apt-get install -y iptables-persistent

echo  "[+] Applying inbound firewall rules"
iptables -I INPUT 1 -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT
iptables -A INPUT -j DROP

echo  "[+] Applying outbound firewall rules"
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --dport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT
iptables -A OUTPUT -j DROP

echo  "[+] Saving firewall rules"
service netfilter-persistent save

echo  "[+] Disabling IPv6"
echo  "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
echo  "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=""/GRUB_CMDLINE_LINUX_DEFAULT="ipv6.disable=1"/' /etc/default/grub
sed -i 's/GRUB_CMDLINE_LINUX=""/GRUB_CMDLINE_LINUX="ipv6.disable=1"/' /etc/default/grub
update-grub

echo  "[+] Configuring hostname"
hostnamectl set-hostname wales
cat <<  EOF > /etc/hosts
127.0.0.1 localhost
127.0.0.1 wales
EOF

echo  "[+] Disabling history files"
ln -sf /dev/null /home/$USER/.bash_history
ln -sf /dev/null /root/.bash_history

echo  "[+] Setting passwords"
echo  "root:--" | chpasswd

echo  "[+] Dropping flags"
echo  "--" > /root/proof.txt
echo  "--" > /home/$USER/local.txt
chmod 0600 /root/proof.txt
chmod 0644 /home/$USER/local.txt
chown $USER:$USER /home/$USER/local.txt

echo  "[+] Cleaning up"
rm -rf /build.sh
rm -rf /root/.cache
rm -rf /root/.viminfo
find /var/log -type f -exec sh -c "cat /dev/null > {}"  \;
```

## Building the Image

My initial submission just included the build script, but someone from the team contacted me and told me they were running into issues with the build script.

I ended up resubmitting with a `.ova` file that I built from a fresh copy of Ubuntu 20.04 and running the install script from the root account. Afterwards I just exported the image through VirtualBox.

I did end up creating a highly complex build script that I will save for another post. It basically uses [Packer](https://github.com/hashicorp/packer), [subiquity](https://github.com/canonical/subiquity), and a bunch of scripts from the [bento](https://github.com/chef/bento) project to automate the build process of the `.ova` virtual machine.

I highly recommend just building the image manually to save a lot of headaches and maybe you'll even be able to get some sunlight today.

## Conclusion

This might be a smart gig for you to take on. But remember to compartmentalize your time and not obesses over little details or do overly-complicated steps. Just make a plan and execute it.
