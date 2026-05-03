# Mocked katakana converter to avoid MeCab dependency issues on Python 3.14
def katakana_converter(text):
    # Simply return the text as is. 
    # The original implementation converted English words to Katakana for VoiceVox.
    return text