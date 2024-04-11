from translate import Translator


def translates(text: str, from_lan: str, to_lan: str):
    translator = Translator(from_lang=from_lan, to_lang=to_lan)

    translate2 = translator.translate(text)

    return translate2


if __name__ == '__main__':
    a = input()
    b = input()
    c = input()

    print(translates(a, b, c))
