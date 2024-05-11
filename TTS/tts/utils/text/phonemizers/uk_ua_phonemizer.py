from typing import Dict
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_UK_PUNCS = ".,!?;:()[]"

class UK_UA_Phonemizer(BasePhonemizer):
    """🐸TTS uk_ua_phonemizer using the IPA-Uk library

    Example:

        >>> from TTS.tts.utils.text.phonemizers import UK_UA_Phonemizer
        >>> phonemizer = UK_UA_Phonemizer()
        >>> phonemizer.phonemize("Це тестове речення для перевірки фонемізації.", separator="|")
        'IPA representation of the Ukrainian sentence'
    """

    language = "uk-UA"

    def __init__(self, punctuations=_DEF_UK_PUNCS, keep_puncs=True, **kwargs):
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "uk_ua_phonemizer"

    def _phonemize(self, text: str, separator: str = "|") -> str:
        from ipa_uk import pronunciation
        ph = pronunciation(text)
        return separator.join(ph)

    def phonemize(self, text: str, separator: str = "|", language=None) -> str:
        return self._phonemize(text, separator)

    @staticmethod
    def supported_languages() -> Dict:
        return {"uk-UA": "Ukrainian"}

    def version(self) -> str:
        return "0.1.0"

    def is_available(self) -> bool:
        try:
            from ipa_uk import pronunciation
            return True
        except ImportError:
            return False

if __name__ == "__main__":
    text = "Це тестове речення для перевірки фонемізації."
    phonemizer = UK_UA_Phonemizer()
    print(phonemizer.supported_languages())
    print(phonemizer.version())
    print(phonemizer.language)
    print(phonemizer.name())
    print(phonemizer.is_available())
    print(phonemizer.phonemize(text))
