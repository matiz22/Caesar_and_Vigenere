
# Caesar and Vigenere

## Overview

Welcome to this simple Python implementation of the Caesar cipher and Vigenère cipher, designed for encryption, decryption, and cracking text.

## Features:

### Caesar Cipher:
* Encryption with customizable shift values
* Decryption with known shift values
* Cracking with best-answer suggestions powered by Olllama
### Vigenère Cipher:
* Encryption with specified keys
* Decryption with known keys
* Cracking with random key selection


### Sample CLI
```bash
python caeser.py encrypt "hello" 3
python caesar.py decrypt "khoor" 3
python caesar.py crack "khoor"

python vigenere.py encrypt "Hello" -k "key"
python vigenere.py decrypt "EncryptedText" -k "key"
python vigenere.py crack "Ciphertext"
```
#### Important Notes:

* Case Sensitivity: Both ciphers operate on lowercase text only.
* Spaces: The tools do not handle spaces within text.
* Environment File: If present, the .env file contains configuration settings.
