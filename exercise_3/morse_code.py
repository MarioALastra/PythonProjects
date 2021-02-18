#   Morse Code
#   Driver: Mario Lastra (U43655957) Navigator: Tilak Patel (U32922919)
#   This script will convert a string into morse code

code = (
    " ", "--..--", ".-.-.-", "..--..",
    "-----", ".----", "..---", "...--",
    "....-", ".....", "-....", "--...",
    "---..", "----.", ".-", "-...", "-.-.",
    "-..", ".", "..-.", "--.", "....", "..",
    ".---", "-.-", ".-..", "-.", "---", ".---.",
    "--.-", ".-.", "...", "-", "..-", "...-", ".--",
    "-..-", "-.--", "--.."
)

user_input = input("Enter the string to be converted to Morse code: ")
user_input = user_input.upper()
final_output = ""

for char in user_input:
    if char == " ":
        final_output += code[0]
    elif char == ",":
        final_output += code[1]
    elif char == ".":
        final_output += code[2]
    elif char == "?":
        final_output += code[3]
    elif char == "0":
        final_output += code[4]
    elif char == "1":
        final_output += code[5]
    elif char == "2":
        final_output += code[6]
    elif char == "3":
        final_output += code[7]
    elif char == "4":
        final_output += code[8]
    elif char == "5":
        final_output += code[9]
    elif char == "6":
        final_output += code[10]
    elif char == "7":
        final_output += code[11]
    elif char == "8":
        final_output += code[12]
    elif char == "9":
        final_output += code[13]
    elif char == "A":
        final_output += code[14]
    elif char == "B":
        final_output += code[15]
    elif char == "C":
        final_output += code[16]
    elif char == "D":
        final_output += code[17]
    elif char == "E":
        final_output += code[18]
    elif char == "F":
        final_output += code[19]
    elif char == "G":
        final_output += code[20]
    elif char == "H":
        final_output += code[21]
    elif char == "I":
        final_output += code[22]
    elif char == "J":
        final_output += code[23]
    elif char == "K":
        final_output += code[24]
    elif char == "L":
        final_output += code[25]
    elif char == "M":
        final_output += code[26]
    elif char == "N":
        final_output += code[27]
    elif char == "O":
        final_output += code[28]
    elif char == "P":
        final_output += code[29]
    elif char == "Q":
        final_output += code[30]
    elif char == "R":
        final_output += code[31]
    elif char == "S":
        final_output += code[32]
    elif char == "T":
        final_output += code[33]
    elif char == "U":
        final_output += code[34]
    elif char == "V":
        final_output += code[35]
    elif char == "W":
        final_output += code[36]
    elif char == "X":
        final_output += code[37]
    elif char == "Y":
        final_output += code[38]
    elif char == "Z":
        final_output += code[39]
    else:
        final_output += char

print(final_output, sep='', end='')
