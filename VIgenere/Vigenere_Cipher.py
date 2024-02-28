from Caesar.Caesar import Caesar
from data.Validate_Text import TextTransformator


class VigenereCipher:
    @staticmethod
    def encrypt(text, key):
        key_ints = TextTransformator.to_ascii(key)
        ciphertext = ''
        for i in range(len(text)):
            shift = key_ints[i % len(key_ints)]
            ciphertext += Caesar.encrypt(text[i], shift)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        key_ints = TextTransformator.to_ascii(key)
        text = ''
        for i in range(len(ciphertext)):
            shift = key_ints[i % len(key_ints)]
            text += Caesar.decrypt(ciphertext[i], shift)
        return text

    @staticmethod
    def crack(ciphertext, max_attempts: int = 12000):
        possible_keys = [(chr(i), chr(j), chr(k)) for i in range(97, 123) for j in range(97, 123) for k in
                         range(97, 123)]
        if max_attempts < len(possible_keys):
            for key in possible_keys:
                decrypted_text = VigenereCipher.decrypt(ciphertext, ''.join(key))
                print(f'Key:{key} Value:{decrypted_text}')
