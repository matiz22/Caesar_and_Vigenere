from Caesar.Caesar import Caesar
import argparse


def encrypt_command(args):
    encrypted_text = Caesar.encrypt(args.text, args.shift)
    print("Encrypted text:", encrypted_text)


def decrypt_command(args):
    decrypted_text = Caesar.decrypt(args.text, args.shift)
    print("Decrypted text:", decrypted_text)


def crack_command(args):
    cracked_text = Caesar.crack_caesar(args.text)
    print("Cracked text:", cracked_text)


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher CLI")

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt text")
    encrypt_parser.add_argument("text", type=str, help="Text to encrypt")
    encrypt_parser.add_argument("shift", type=int, help="Shift value for encryption")
    encrypt_parser.set_defaults(func=encrypt_command)

    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt text")
    decrypt_parser.add_argument("text", type=str, help="Text to decrypt")
    decrypt_parser.add_argument("shift", type=int, help="Shift value for decryption")
    decrypt_parser.set_defaults(func=decrypt_command)

    crack_parser = subparsers.add_parser("crack", help="Crack Caesar cipher")
    crack_parser.add_argument("text", type=str, help="Text to crack")
    crack_parser.set_defaults(func=crack_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
