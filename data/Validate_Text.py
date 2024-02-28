class TextTransformator:
    @staticmethod
    def to_ascii(text: str) -> list:
        possible = range(97, 122)
        return [ord(c) for c in text.lower() if ord(c) in possible or not c.isspace()]

    @staticmethod
    def from_ascii(ascii_int: list) -> str:
        val = ''
        for i in ascii_int:
            val += chr(i)
        return val
