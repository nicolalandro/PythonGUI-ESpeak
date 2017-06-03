import os


def speack(string, language):
    if language == 1:
        uno = 'espeak -v it "'
    else:
        uno = './simple-google-tts/simple_google_tts it "'
    due = string
    tre = '"'

    discorso = uno + due + tre
    discorso = discorso

    os.system(discorso)


def speack_from_file(string, language):
    if language == 1:
        uno = 'espeak -v it -f "'
        tre = '"'
    else:
        uno = './simple-google-tts/simple_google_tts it '
        tre = ''
    due = string

    discorso = uno + due + tre
    discorso = discorso

    os.system(discorso)
