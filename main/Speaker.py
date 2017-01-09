import os


def speack(string, language):
    if language == 1:
        uno = 'espeak -v mb-it4 "'
    else:
        uno = 'espeak -v it "'
    due = string
    tre = '"'

    discorso = uno + due + tre
    discorso = discorso.encode("utf8")

    os.system(discorso)