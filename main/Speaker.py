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