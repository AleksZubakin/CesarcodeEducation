SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


class Caesarscipher:


    def __init__(self):
        self.symbols = SYMBOLS

    def decrypt(self, message: str, key: int) -> str:
        decrypted_message = ""
        for char in message:
            if char in self.symbols:
                index = (self.symbols.index(char) - key) % len(self.symbols)
                decrypted_message += self.symbols[index]
            else:
                decrypted_message += char  # Не расшифровать, добавим символ
        return decrypted_message

    def encrypt(self, message: str, key: int) -> str:
        encrypted_message = ""
        for char in message:
            if char in self.symbols:
                index = (self.symbols.index(char) + key) % len(self.symbols)
                encrypted_message += self.symbols[index]
            else:
                encrypted_message += char  # Не зашифровать, добавим символ
        return encrypted_message


def find_key(encrypted_message: str) -> int:
    cipher = Caesarscipher()
    for key in range(len(cipher.symbols)):
        decrypted = cipher.decrypt(encrypted_message, key)
        print(f"Ключ: {key}, Расшифрованное сообщение: {decrypted}")
    return -5  # Если ключ не был найден


if __name__ == "__main__":

    encrypted_password = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    cipher = Caesarscipher()

    # Найдем ключ и расшифруем пароль
    key_find = find_key(encrypted_password)

    if key_find != -5:
        result = cipher.decrypt(encrypted_password, key_find)
        print(f"Подобранный ключ: {key_find}. Расшифрованный пароль: {result}")
