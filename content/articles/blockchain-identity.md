Title: Verifying Identification on the Blockchain
Date: 2022-03-30 22:30
Category: Ethereum, Blockchain
Tags: ethereum, blockchain
Author: hexcowboy
Summary: Ideating on the concept of connecting social media and identity to your blockchain address

A long-lasting issue on the blockchain has been reliably linking your identity to your wallet. There are many reason you may want to do this, including:

- Paying internet money to a social media account (and not your 40 character hex address)
- Getting the identity of a wallet address in order to contact the owner
- Using assets like NFTs to gain access to exclusive content based on reputation or previous social interactions

Other projects have tried to solve this issue. An example would be ENS, where you may create a new identity similar to a classic domain name like `hexcowboy.eth`. This approach is the most holistic but ignores a few important things.

1. Having a domain name does not appeal to everyone's identity
2. Not everybody wants to pay a subscription cost to maintain their identity
3. Most people already have built reputation on other platforms with their identity

## Using Pre-existing Services to Identify Yourself

> The majority of this article will use Twitter as an example. There are obviously other use cases like other social media accounts or even government issued documents.

For almost two decades now, millions of people have been building reputation on their social media accounts. People are able to express themselves through their online identity. In many cases this online identity provides perks to them such as access to exclusive chatrooms, invitations to private events, or sometimes just clout. It would only make sense to use these pre-existing identities as leverage to onboard new users.

To do this, a simple model can be used. The process is as follows:

1. A **proof** is submitted to the user's social media account containing a signed message containing the username (or user ID, whichever is immutable)
2. The ID of the post is submitted to a smart contract
3. Anyone may reach out to the smart contract to retrieve the proof ID, where they may then use the social media APIs to verify the signed message's signer

A few caveats:

- The proof must always remain available, meaning that if the proof post is ever deleted, the account is ever made private, or in the case of any other form of censorship, it would trigger the verifiers to fail
- The verifier of the proof will usually have to work off-chain, as it's not possible to trustlessly reach out to APIs from the blockchain virtual machine

## Technical Specification

### Creating an Identity Proof

A proof contains an [EIP-191](https://eips.ethereum.org/EIPS/eip-191) signed message Using Ethers.js as a client library, a user can sign a message with their wallet:

```js
const provider = new ethers.providers.Web3Provider(web3Provider.provider);
const signer = provider.getSigner();
signer.signMessage("hexcowboy").then(async (message) => {
  // This is pseudo-code representing a call to the Twitter API to post a tweet with the signed message
  const tweet = await twitterClient.tweet(message);
  // The Tweet ID would be used to submit the proof
  console.log("Tweet ID: " + tweet.id);
});
```

### Submitting an Identity Proof

The following is an example of how a Twitter proof registry could be implemented:

```solidity
contract TwitterRegistry {
	mapping(bytes32 => address) private records;

	event ProofSubmitted(address indexed _from, bytes32 indexed _proof);

	function submitProof(bytes32 data) external {
		records[data] = msg.sender;
		emit ProofSubmitted(msg.sender, data);
	}
}
```

This is similar to an ERC-721 implementation where a "token" is mapped to an address. In this case, the bytes32 representation of the post ID is mapped to an address and a `ProofSubmitted` event is emitted so indexers can easily find all proofs a specific address has submitted.

### Verifying a Proof

Anyone can verify a proof if they need to. Obviously users can submit arbitrary or malicious data to claim their proof but because signed messages use cryptography, the signer's address can be recovered and in turn prevent fraud.

Here is a Golang implementation to verify a proof:

```go
package helpers

import (
	"context"
	"errors"
	"strconv"

	"github.com/ethereum/go-ethereum/common/hexutil"
	"github.com/ethereum/go-ethereum/crypto"
)

// Provided the original message text (`message`) and the signed messaged (`signedMessage`), returns the signer's public key as a string
func VerifyMessage(ctx context.Context, message string, signedMessage string) (string, error) {
	// Hash the unsigned message using EIP-191 message format
	hashedMessage := []byte("\x19Ethereum Signed Message:\n" + strconv.Itoa(len(message)) + message)
	hash := crypto.Keccak256Hash(hashedMessage)

	// Get the bytes of the signed message
	decodedMessage := hexutil.MustDecode(signedMessage)

	// Handles cases where EIP-115 is not implemented (most wallets don't implement it)
	if decodedMessage[64] == 27 || decodedMessage[64] == 28 {
		decodedMessage[64] -= 27
	}

	// Recover a public key from the signed message
	sigPublicKeyECDSA, err := crypto.SigToPub(hash.Bytes(), decodedMessage)
	if sigPublicKeyECDSA == nil {
		err = errors.New("Could not get a public get from the message signature")
	}
	if err != nil {
		return "", err
	}

	return crypto.PubkeyToAddress(*sigPublicKeyECDSA).String(), nil
}
```

_The code handles issues with EIP-115 not being implemented, which Ethers.js (used in the "Creating an Identity Proof" section) does not._

## Additional Questions and Ideas

A few questions and answers I've made up to help better understand the reasons for my implementations.

> **Q**: Why don't we use something like an oracle to submit the user's username to the blockchain?
> **A**: By nature oracles are not trustless. It is possible to do a somewhat decentralized implementation using oracle networks but it's a far more complicated topic and even networks like Chainlink don't provide solutions for decentralized API calls in this fashion.

> **Q**: Why can't the proof post be immutable?
> **A**: The proof has to be as close as possible to the nature of the blockchain for it to play by the blockchain's rules.

> **Q**: Can't I just submit a proof to someone else's Tweet (proof post) to claim their Twitter identity?
> **A**: No, since the public key is always cryptographically recovered from the signed message it's not possible to spoof it.

> **Q**: If for some reason my account is deleted or my proof post is deleted out of my control, is my identity still valid?
> **A**: If the proof post is not accessible to verifiers for _any_ reason, it's not valid.

> **Q**: How would documents like government IDs be validated?
> **A**: That's a good question, and if you think of a solution we should get in contact.

### Additional use cases for identity proofs

- Airdrops for people who have completed a specific social interaction like followed an account, tweeted about a topic, or similar
- Easily link to social profiles on NFT marketplaces
- Exclusive access to Discord servers
- Look up a social media user's NFTs
