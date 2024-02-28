import argparse
from VIgenere.Vigenere_Cipher import VigenereCipher

def main():
    parser = argparse.ArgumentParser(description='Vigenere Cipher Tool')
    parser.add_argument('action', choices=['encrypt', 'decrypt', 'crack'], help='Action to perform: encrypt, decrypt, or crack')
    parser.add_argument('text', help='Text to process')
    parser.add_argument('-k', '--key', help='Key to use (required for encrypt and decrypt actions)')
    parser.add_argument('-m', '--max-attempts', type=int, default=12000, help='Maximum attempts for cracking (default: 12000)')

    args = parser.parse_args()

    if args.action == 'encrypt':
        if args.key is None:
            parser.error('Key is required for encryption.')
        encrypted_text = VigenereCipher.encrypt(args.text, args.key)
        print('Encrypted Text:', encrypted_text)
    elif args.action == 'decrypt':
        if args.key is None:
            parser.error('Key is required for decryption.')
        decrypted_text = VigenereCipher.decrypt(args.text, args.key)
        print('Decrypted Text:', decrypted_text)
    elif args.action == 'crack':
        print('Possible Decryptions:')
        VigenereCipher.crack(args.text, args.max_attempts)


if __name__ == '__main__':
    main()
