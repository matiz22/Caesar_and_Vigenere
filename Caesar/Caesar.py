from data.Ollama import Ollama
from data.Validate_Text import TextTransformator


class Caesar:

    @staticmethod
    def encrypt(text: str, shift: int) -> str:
        to_be_encrypted = TextTransformator.to_ascii(text)

        for i in range(len(to_be_encrypted)):
            to_be_encrypted[i] = (to_be_encrypted[i] + shift - 97) % 26 + 97

        return TextTransformator.from_ascii(to_be_encrypted)

    @staticmethod
    def decrypt(text: str, shift: int) -> str:
        return Caesar.encrypt(text, shift * -1)

    @staticmethod
    def crack_caesar(text: str) -> str:
        possible_answers = []
        print('Possible combination')
        for i in range(26):
            decrypted = Caesar.decrypt(text, i)
            possible_answers.append(decrypted)
            print(decrypted)

        return Ollama.get_ollama_response(possible_answers)
