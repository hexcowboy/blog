Title: Loot Oracles and an Introduction to Loot St
Date: 2021-09-14 8:00
Category: Ethereum
Tags: ethereum, nft, loot
Author: hexcowboy
Summary: Turn legacy NFTs into Loot items with Oracles and witchcraft

A new problem has manifested in the Metaverse. Through a combination of verifiable ownership and Bitcoin maxi resistance, NFT "profile pictures" or PFPs on Ethereum and other Smart Contract blockchains are selling for as high as [$7 million dollars](https://www.larvalabs.com/cryptopunks/details/3100). Some classic examples of PFPs include CryptoPunks, Bored Ape Yacht Club, and CryptoToadz.

![CryptoPunks](https://www.larvalabs.com/public/images/product/cryptopunks/punk-variety-2x.png)

Although there are 10,000 different combinations of unique CryptoPunks, there is currently no way to customize your CryptoPunk. If your punk is purchased without a cowboy hat, you may never expect to see a cowboy hat on its head.

Loot Oracles are the first solution to this problem. To understand what the hell a Loot Oracle is, it's necessary for me to define these two words.

**Loot**: An ERC1155 NFT that can potentially be used to represent part of a character. _(Not to be confused with [a black square with text on it](https://opensea.io/collection/lootproject))_

**Oracle**: An off-chain program that can inject data into a blockchain. It is usually paired with a Smart Contract or it reads events from the blockchain.

Therefore, a Loot Oracle can be used to create Loot while reading data from the blockchain. This Loot can then be reused to make characters or trade on secondary marketplaces like [OpenSea](https://opensea.io/).

_Bottom Line_: Loot can be used to create a custom PFP with swappable attributes.

![enter image description here](https://images.squarespace-cdn.com/content/v1/59413d96e6f2e1c6837c7ecd/1516201738494-52HYDY308LP4GZA1AMDL/Crypto_Animation.gif)

## Introduction to Loot St

Loot St is probably my coolest project of 2021 and is the first interface made for Loot Oracles. Right now it is in a live beta at [beta.loot.st](https://beta.loot.st) as a simple demo for how you can turn a CryptoPunk into Loot.

For this example, I will be pretending to own [Punk #5066 ![enter image description here](https://www.larvalabs.com/public/images/cryptopunks/punk5066.png)](https://www.larvalabs.com/cryptopunks/details/5066).

This CryptoPunk has three attributes: Earring, Knitted Cap, and Smile. When I convert the CryptoPunk to Loot, I will be getting all of these attributes as separate NFTs plus an additional Zombie head.

![Zombie Head](https://ipfs.io/ipfs/Qmb32q3F2GYcqeqnAPEobyAxCL45SSrVVQcJCxFpfCQU3H/ZOMBIE.gif)

![Earring](https://ipfs.io/ipfs/Qmb32q3F2GYcqeqnAPEobyAxCL45SSrVVQcJCxFpfCQU3H/EARRING.gif)

![Knitted Cap](https://ipfs.io/ipfs/Qmb32q3F2GYcqeqnAPEobyAxCL45SSrVVQcJCxFpfCQU3H/KNITTED_CAP.gif)

![Smile](https://ipfs.io/ipfs/Qmb32q3F2GYcqeqnAPEobyAxCL45SSrVVQcJCxFpfCQU3H/SMILE.gif)

Each of these items will be separately tradable and can be viewed in any application that supports ERC1155 balances, like OpenSea.

### Wrapping the CryptoPunk

For most NFTs, this step is omitted. Since CryptoPunks were created before the NFT standard (ERC721), they need to be converted to an ERC721 token. Luckily LarvaLabs has already put together an application that handles this process, called [WrappedPunks](https://wrappedpunks.com/).

I also wrote this process directly into beta.loot.st which means you don't even have to leave the application. It's literally no different than wrapping your punk on wrappedpunks.com, just a different user interface.

1. **Register** a proxy
2. Send the CryptoPunk to the proxy (**Wrap**)
3. Mint the WrappedPunk (**Mint**)

Both beta.loot.st/wrap and wrappedpunks.com will walk you through the process, although you may only access wrappedpunks.com on Mainnet while Loot St is available on the Rinkeby testnet.

### Claiming Loot

Now even though I made fun of the black squares with text on them before, the creator of "Loot (for Adventurers)", there is some awesome discussion going on at [Loot Talk](https://loot-talk.com/) which was created by the same person. This is where I found the idea of a loot claim.

Basically a Loot Claim takes 1 NFT with pre-compose Loot and breaks down the Loot into separate NFTs. That is exactly what Loot St does on the beta.loot.st/loot page.

Because CryptoPunks (as well as many NFTs) do not store their traits on-chain, an Oracle must be used to calculate these traits and inject the data into the blockchain. The Oracle unfortunately cannot do this for free and must pay gas to inject data, therefore the Oracle needs to be funded.

On beta.loot.st, the funding cost is 0.1 ETH. Although this is high, it is a safeguard against [ridiculously high network fees that we've recently seen](https://bitcoinist.com/ethereum-gas-fees-skyrocket-is-this-the-season-of-the-eth-killers/) during network surges.

There are three players in this:

- The NFT owner (user)
- The Oracle contract
- The Oracle server

Once the Oracle is funded, it can then start receiving NFTs. The process is basically as follows:

1. The user sends an NFT to the Oracle contract
2. The Oracle server listens for the event "ERC721Received" or "ERC1155Received"
3. Once the event is found, the Oracle server then mints the new Loot items to the original user

### Caveats

The process is straightforward and easy for the end user. However, right now the backend is a bit complicated. There remain a few caveats:

#### The NFT Loot Oracle is not bidirectional (yet)

I say _yet_ because it is possible to put this logic into the contract. In the beta I just wanted to get the most basic product out to see if it was interesting.

#### The Oracle could be run by a malicious operator that mints arbitrary items, so it is best if the operator is the original issuer of the NFT

One proposal is to use ChainLink to fetch data from an IPFS API. This way, the data is verifiably true and ChainLink can provide consensus on which data is correct, meaning there is no malicious action.

### Links

GitHub: [https://github.com/hexcowboy/punk-loot](https://github.com/hexcowboy/punk-loot)

Discord: [https://discordapp.com/users/418557177825853443](https://discordapp.com/users/418557177825853443)

Loot St Beta: [https://beta.loot.st/](https://beta.loot.st/)
