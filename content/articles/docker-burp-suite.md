Title: Running Burp Suite in Docker
Date: 2021-06-13 10:30
Category: Docker
Tags: docker, burpsuite
Author: hexcowboy
Summary: Quickly install Burp Suite on Docker in a matter of seconds, not minutes.

On my soul quest to create [a fully featured penetration testing Docker container](https://github.com/hexcowboy/saloon), I came across a few issues.

1. Docker doesn't run graphical applications on it's own
2. The network proxy won't work unless the `8080` port is exposed
3. You can't just install Burp Suite with `apt-get install burpsuite`

Apart from these issues, there isn't a maintained Burp Suite Community repository in the Docker Hub or on GitHub. I did manage to find a maintained [Burp Suite Professional Docker repo](https://github.com/koenrh/docker-burp-suite-pro) on GitHub which I ended up forking.

## Setup

To make this Docker container run GUI applications, we can make use of an X Server. On macOS, I used [XQuartz](https://www.xquartz.org/) which was as simple as running

```bash
brew install --cask xquartz
```

For accepting connections on local host, one setting needs to be changed. In the XQuartz settings, enable `XQuartz` > `Preferences` > `Security` > `Allow connections from network clients`.

![Allow connections from network clients needs to be enabled in the XQuartz settings]({static}/images/allow-connections.png)

Now the X Server can be started by running this command:

```bash
xhost + 127.0.0.1
```

*Note that you need to run this command from your host terminal, not the XQuartz terminal.*

I won't go into covering how to run a local X Server on Windows or Linux, because Google **does** exist.

## Running Burp Suite

### From Docker Hub

The prebuilt container can be retrieved from [Docker Hub](https://hub.docker.com/repository/docker/hexcowboy/burpsuite).

```bash
docker pull hexcowboy/burpsuite
docker image tag hexcowboy/burpsuite burpsuite
```

### Building the image

First, clone this [GitHub repository](https://github.com/hexcowboy/docker-burp-suite-community) on your host:

```bash
git clone https://github.com/hexcowboy/docker-burp-suite-community.git && cd docker-burp-suite-community
```

Then, build the Docker image using the following command.

```bash
docker build -t burpsuite .
```

While building the image, the latest JAR (Java ARchive) of Burp Suite Community is pulled from the PortSwigger portal.

## Using Burp Suite Community

```bash
docker run --rm \
  -p 8080:8080 \
  burpsuite
```

This command will run the container, expose port 8080 on the host to port 8080 on the container, and delete the container afterwards. You should see a new window open up in your X Server if you followed the setup instructions above.

### Verify that the proxy is working by running the following command on your host:

```bash
curl -x http://127.0.0.1:8080 http://example.com
```

## Conclusion

Software can easily be Dockerized. Burp Suite Community could likely take 5+ minutes to install manually, but by pulling a prebuilt Docker image it can take just seconds.

The future of the west is Dockerized.
