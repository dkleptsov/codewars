MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_bits(bits: str) -> str:
    bits = bits.strip("0")
    speed = detect_shortest(bits)
    for bit, char in [("1"*3*speed, "-"), ("1"*speed, "."),("0"*7*speed, "   "), ("0"*3*speed, " "), ("0"*speed, "")]:
        bits = bits.replace(bit, char)
    return bits


def detect_shortest(bits: str) -> int:
    zeros = sorted([len(x) for x in bits.split("1") if x])
    ones = sorted([len(x) for x in bits.split("0") if x])
    if zeros and ones: return min(zeros[0], ones[0])
    elif zeros: return zeros[0]
    elif ones: return ones[0]


def decode_morse(morse_code: str) -> str:
    return ' '.join(''.join(MORSE_CODE.get(char, "") for char in word.split(" ")) for word in morse_code.strip().split("   "))


# https://www.codewars.com/kata/54b72c16cd7f5154e9000457