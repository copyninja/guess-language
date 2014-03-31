from guess_language import guessLanguageName, guessLanguage, NAME_MAP
from silpa_common.langdetect import detect_lang


def _getName(lang):
    return NAME_MAP.get(lang, 'UNKNOWN')


class LangGuess:
    def guessLanguage(self, text):
        lang = guessLanguageName(text)
        if lang == 'UNKNOWN':
            firstWord = text.split()[0]
            lang = detect_lang(firstWord)[firstWord]
            lang = _getName(lang.split("_")[0])
        return lang

    def guessLanguageId(self, text):
        lang = guessLanguage(text)
        if lang == 'UNKNOWN':
            firstWord = text.split()[0]
            lang = detect_lang(firstWord)[firstWord]
        return lang

    def getScriptName(self, text):
        return detect_lang(text)

    def get_module_name(self):
        return "Guess Language"

    def get_info(self):
        return "Guess the language of given text. This module can" + \
            "detect more than 50 languages. Based on Language::Guess by" + \
            "Maciej Ceglowski (http://languid.cantbedone.org/)"


def getInstance():
    return LangGuess()
