import requests
import os


def translate_it(from_file, to_file, from_lang, to_lang):
    with open(from_file) as f:
        text = f.read()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    lang_string = from_lang + '-' + to_lang
    params = {
        'key': key,
        'lang': lang_string,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    result_text = ' '.join(response.get('text', []))
    write_file(to_file, result_text)
    return None


def write_file(file_name, file_text):
    with open(file_name, 'w') as f:
        f.write(file_text)
    print('Перевод записан в файл {}'.format(file_name))


def check_result_folder(check_dir):
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
        print('Создан каталог {}'.format(check_dir))


def main():
    result_dir = 'Result'
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_dir)
    check_result_folder(result_dir)   # Каталог для сохранения результата перевода

    my_dir = ""
    my_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), my_dir)   # Исходный каталог

    my_format_file = '.txt'
    list_files = {os.path.join(my_dir, f): f.split('.')[0].lower() for d, dirs, files in os.walk(my_dir)
                  for f in files if f.endswith(my_format_file)}  # Создаем список исх. файлов и языка перевода
    print('Всего {} txt файлов для перевода'.format(len(list_files)))

    for translate_file, from_lang in list_files.items():
        to_lang = 'ru'
        result_file = from_lang + '_' + to_lang + '.txt'
        result_file = os.path.join(result_dir, result_file)
        translate_it(translate_file, result_file, from_lang, to_lang)


if __name__ == '__main__':
    main()
