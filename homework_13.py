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
    results = []  # Список для хранения ключей и расшифрованных сообщений

    for key in range(len(cipher.symbols)):
        decrypted = cipher.decrypt(encrypted_message, key)
        results.append((key, decrypted))  # Добавляем результат в список
        print(f"Ключ: {key}, Расшифрованное сообщение: {decrypted}")

    return results

def save_to_file(results: list, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        for key, decrypted_message in results:
            file.write(f"Ключ: {key}, Расшифрованное сообщение: {decrypted_message}\n")


if __name__ == "__main__":

    encrypted_password = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    cipher = Caesarscipher()

    results = find_key(encrypted_password)

    save_to_file(results, 'keys_result.txt')

    if results:
        key, result = results[0]  # или любой другой ключ
        print(f"Подобранный ключ: {key}. Расшифрованный пароль: {result}")
