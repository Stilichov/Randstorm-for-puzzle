\# Randstorm-for-puzzle

Between 2010 and 2015, many exchanges and websites relied on BitcoinJS-lib v0.1.3 for Bitcoin wallet generation. The issue was that many browsers didn't use window.crypto.random, which lead to entropy being collected from Math.random().

More details can be found in below repo.

https://github.com/RandstormBTC/randstorm?tab=readme-ov-file

The ~1000 BTC Bitcoin Challenge Transaction  was created in 2015 and there is a chance that the wallets were created with math.random() 

Currently I am using pythons random function random.randint((0, 65535))  in place of  javascripts t = Math.floor(65536 \* Math.random());

However this needs to be adapted as old versions of Math.random()  did not really give fully random numbers. 

Todo:

Implement the vulnerable Math.random from old browser versions. 

Enable multiprocessing for parallel processing of different time 

Convert to C,C++ for better performance.


**Dependence**

https://github.com/iceland2k14/secp256k1

**How to use**

download iceland2k14/secp256k1 and place ice\_secp256k1.dll  or ice\_secp256k1.so together with secp256k1.py in the project folder

for puzzle 66 which has key length of 66 bits get the first transaction time  ie 1/15/2015, 13:07:14. Which means that the wallet was created anytime before that. 

Convert this time to unix format in miliseconds.  Here https://www.unixtimestamp.com/

Which translates to 1421345114000

"Usage: python script.py <seed\_time\_value> <target\_address> <key\_length\_in\_bytes> <loop\_count>" 

run python randstorm-puzzle.py 1421345114000 13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so 66 100000

**Disclaimer**

This software is for education purposes only and should not be configured and used to find (Bitcoin/Altcoin) address hash (RIPEMD-160) collisions and use (steal) credit from third-party (Bitcoin/Altcoin) addresses. This mode might be allowed to recover puzzle private keys or public addresses only.

