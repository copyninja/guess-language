from guesslanguage import getInstance
import sys

if sys.version_info.major == 3:
    import uprefix
    uprefix.register_hook()


lang_guesser = getInstance()


def test_guessLanguage():
    "TEST: guessLanguage function"
    assert lang_guesser.guessLanguage(u"ನಮಸ್ಕಾರ") == "Kannada"
    assert lang_guesser.guessLanguage(u"വാസുദേവ") == "Malayalam"
    #TODO add more language strings


def test_guessLanguageId():
    "TEST: guessLanguageId function"
    assert lang_guesser.guessLanguage(u"ನಮಸ್ಕಾರ") == "kn"
    assert lang_guesser.guessLanguage(u"വാസുദേവ") == "ml"
    #TODO add more language strings
