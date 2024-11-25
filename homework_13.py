import enchant
import time

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


class Caesarscipher:

    def __init__(self):
        self.symbols = SYMBOLS

    def decrypt(self, message: str, key) -> str:
        decrypted_message = ""
        for char in message:
            if char in self.symbols:
                index = (self.symbols.index(char) - key) % len(self.symbols)
                decrypted_message += self.symbols[index]
            else:
                decrypted_message += char  # Не расшифровать, добавим символ
        return decrypted_message

    def encrypt(self, message: str, key) -> str:
        encrypted_message = ""
        for char in message:
            if char in self.symbols:
                index = (self.symbols.index(char) + key) % len(self.symbols)
                encrypted_message += self.symbols[index]
            else:
                encrypted_message += char  # Не зашифровать, добавим символ
        return encrypted_message

    def check_decrypt(self, message: str, key: int):
        d = enchant.Dict('en_US')
        i = 0
        phrase = message
        summary = message
        decrypt_list = []

        for _ in self.symbols:
            left_phrase = phrase
            for _ in message:
                index = phrase.find(' ')
                if index != -1:
                    left_phrase = phrase[0:index]
                    phrase = phrase[index + 1:]
            if d.check(left_phrase):
                decrypt_list = [key + i, summary, phrase]
                return decrypt_list

            else:
                i += 1
                phrase = self.decrypt(message, key + i)
                summary = phrase

    def save_to_file(self, results: str, filename: str) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(results)
        return True


if __name__ == "__main__":

    message_input = str(input('Введите фразу: '))
    str_key = input('Введите ключ, или оставьте пустым: ')
    type_start = str(
        input('введите тип действия(0 - расшифровать, 1 - зашифровать):')
        )
    if type_start != '':
        type_start = int(type_start)
    else:
        type_start = 55

    if str_key != '':
        key = int(str_key)
    else:
        key = 55

    cipher = Caesarscipher()

    if key == 0:
        print('Ключ равен 0. Не шифруем')
    elif key != 55:
        if type_start == 1:
            encrypt = cipher.encrypt(message_input, key)
            result = 'Вы зашифровали фразу' + message_input
            result += '. Результат: ' + encrypt
            print(f'Вы зашифровали фразу: {message_input}', end=' ')
            print(f'. Результат: {encrypt}')
        elif type_start == 0:
            decrypt = cipher.decrypt(message_input, key)
            result = 'Вы расшифровали фразу' + message_input
            result += '. Результат: ' + decrypt
            print(f'Вы расшифровали фразу: {message_input}', end=' ')
            print(f'. Результат: {decrypt}')
    elif key == 55:
        cipher_list = cipher.check_decrypt(cipher.decrypt(message_input, 0), 0)
        result = 'Ваша исходная фраза' + cipher_list[1]
        result += '. Ваш ключ:' + str(cipher_list[0])
        result += '. Возможно ваш пароль: ' + cipher_list[2]
        print(f'Ваша исходная фраза: {cipher_list[1]}.', end=' ')
        print(f'Ваш ключ: {cipher_list[0]}.', end=' ')
        print(f'Возможно ваш пароль: {cipher_list[2]}')

    save = str(input('Сохранить результаты в файл? y//n: '))
    if save == 'y':
        path = str(input('Введите путь и имя файла для сохранения: '))
        if path != '':
            if cipher.save_to_file(result, path):
                time.sleep(3)
                print('Файл успешно сохранен.')
                time.sleep(2)
    else:
        print('Ну нет так нет.')
        time.sleep(1)
