Title: 0xDEADBABE Generating Ethereum Vanity Addresses
Date: 2021-08-05 8:00
Category: Ethereum
Tags: ethereum
Author: hexcowboy
Summary: Generate an ethereum address of your liking with a tool called Profanity

I recently acquired a new ethereum address starting with 0x22222222. The idea came to me when I was viewing ethereum transactions on Etherscan, where it shows the first 8 digits of each address in a transaction list.

To get some inspiration on what your new Ethereum address can look like, brush up on your [Hexspeak](https://en.wikipedia.org/wiki/Hexspeak) and reminisce in your hacked days of `DEADBEEF` buffer overflows.

The methodology is simple in theory: you just need to brute force a bunch of ethereum public/private keypairs until you get a public key that matches your liking. Luckily, in practice, it is also easy thanks to a tool called [profanity](https://github.com/johguse/profanity). This tool utilizes your computer's GPU to brute force tens of millions of hashes per second.

To get started, install the following dependencies:

```bash
# Linux
$ apt update && apt install gcc make

# macOS
$ brew install gcc make

# Windows
# Get WSL2 ffs
```

To compile the source, follow these steps:

```bash
# Clone the repository and change to the directory
$ git clone "https://github.com/johguse/profanity.git" profanity && cd $_

# Build it
$ make
```

Profanity is a pretty powerful tool. On my 2017 MacBook Pro, it was able to get around 11 MH/s, meaning 11 million hashes per second. It took me less than 10 minutes to get an address with 8 matching characters. With a dedicated GPU, you could likely get 20-30+ MH/s and start looking at cracking 9 or 10 digit public keys within minutes!

A few examples of how you can use profanity to get the address of your liking are as follows:

```bash
$ ./profanity.x64 --leading 2
-> Addresses starting with 0x2222222

$ ./profanity.x64 --matching DEADBEEF
-> Addresses starting with 0xDEADBEEF

$ ./profanity.x64 --contract 69696969
-> Addresses that will generate their first contract beginning with 0x6969669

$ ./profanity.x64 --matching badXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXbad
-> Addresses starting with 0xBAD and ending in BAD
```

When running these commands, Profanity will show you a bunch of addresses. Each new address will be equal to or better than score, meaning it matched as many characters as it could closest to your request. Don't expect to crack 12 characters any time in the near future, unless you own a Quantum computer in your basement (this article will not age well).

A note before using these addresses: **CHECK TO MAKE SURE THEY WORK**. This means plug the private key into metamask and make sure the public key is what you expected it to be. You will also need to get the correct letter casing before using the addresses' public key. Profanity spits out all public keys in *lowercase*, but Ethereum smart contracts may require them to be in the correct checksum format. This means an `a` in your address is not the same as `A`. To get the correct address checksum, most wallets will automatically figure it out for you, including MetaMask.

Once you've ensured that the address you got is working, you're ready to start using it in transactions!

Happy London Fork 🔥
