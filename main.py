import regularExpression as regEx
import encode as en
# A ceaser cipher that adds to the shift every time a letter changes

def main():
    print("What is the starting shift of the code.")
    shift = int(input())
    print("How much does the shift change every letter")
    change = int(input())


def encrypt_ui(shift, change):
    print("What is the message that you want to encode?")
    message = input()
    buffer = ""
    for i in range(len(message)):
        shift += change
        if shift > 25:
            shift -= 26
        buffer += en.char_encode(message[i], shift)
    print(buffer)

encrypt_ui(13, 2)