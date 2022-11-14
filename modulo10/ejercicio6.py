letter_to_morse = {
    "A": ".-", "B": "-...",
    "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.",
    "G": "--.", "H": "....",
    "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.",
    "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-",
    "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    ".": ".-.-.-", ",": "-.-.--"
}

# entries = [
#     "Hola mundo",
#     "La mariposa revolotea, como si desesperara en este mundo.",
#     "Este es un mensaje programado en Python, pero codificado en morse."
# ]


def morse_decoder(string):
    words = string.split(" ")
    decoded_phrase = ''
    for k in range(len(words)):
        letters = []
        for i in range(len(words[k])):
            letters.append(words[k][i].upper())
            decoded_phrase += letter_to_morse[words[k][i].upper()] + " "

        if k != len(words) - 1:
            decoded_phrase += "/" + " "

    return decoded_phrase + "\n"


def main():
    c = int(input())

    for i in range(c):
        phrase = input()
        result = morse_decoder(phrase)
        # result = morse_decoder(entries[i]) # test only
        print(result)
        # print(result == tests[i]) # test only


main()
