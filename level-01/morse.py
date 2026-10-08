MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '/': '-..-.'
}

# Reverse the dictionary for decoding
REVERSE_MORSE = {code: char for char, code in MORSE_CODE.items()}


def encode(text):
    words = text.upper().split(' ')
    encoded_words = []

    for word in words:
        encoded = []

        for char in word:
            encoded.append(MORSE_CODE.get(char, '?'))

        encoded_words.append(' '.join(encoded))

    return ' / '.join(encoded_words)


def decode(morse):
    words = morse.strip().split(' / ')
    decoded_words = []

    for word in words:
        decoded = []

        for code in word.split():
            decoded.append(REVERSE_MORSE.get(code, '?'))

        decoded_words.append(''.join(decoded))

    return ' '.join(decoded_words)


def main():
    while True:
        print("\nMorse Code Translator")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter text: ")
            print("Morse:", encode(text))

        elif choice == '2':
            morse = input("Enter Morse code: ")
            print("Text:", decode(morse))

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()