import requests
import os


def translate_it(text, from_lang, to_lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    lang_string = from_lang + '-' + to_lang

    params = {
        'key': key,
        'lang': lang_string,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def write_file(file_name, file_text):
    f = open(file_name, 'w')
    for text_to_write in file_text:
        f.write(text_to_write + '\n')
    print('Перевод записан в файл {}'.format(file_name))
    f.close()


def check_result_folder(check_dir):
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
        print('Создан каталог {}'.format(check_dir))


def main():
    result_dir = 'Result'
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_dir)
    check_result_folder(result_dir)   # Каталог для сохранения результата перевода

    list_files = {}
    my_dir = ""
    my_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), my_dir)

    my_format_file = '.txt'
    for d, dirs, files in os.walk(my_dir):
        for f in files:
            if my_format_file in f:
                list_files[os.path.join(my_dir, f)] = f.split('.')[0].lower()
    print('Всего {} txt файлов для перевода'.format(len(list_files)))

    for translate_file, from_lang in list_files.items():
        t = []
        with open(translate_file) as f:
            text = f.read()
            t.append(translate_it(text, from_lang, 'ru'))
            f.close()
        new_file = from_lang + '_ru.txt'
        new_file = os.path.join(result_dir, new_file)
        write_file(new_file, t)


if __name__ == '__main__':
    main()
