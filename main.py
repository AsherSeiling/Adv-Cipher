import regularExpression as regEx
import encode as en
import decode as dec
# A ceaser cipher that adds to the shift every time a letter changes

def main():
    print("What is the starting shift of the code.")
    shift = int(input())
    print("How much does the shift change every letter")
    change = int(input())
    print("Encrypt or decrypt?(en, dc)")
    chose = input()
    if chose == "en":
        encrypt_ui(shift, change)
    else:
        decrypt_ui(shift, change)


def encrypt_ui(shift, change):
    print("What is the message that you want to encode?")
    message = input()
    buffer = ""
    for i in message:
        if regEx.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", i) == True:
            shift += change
            if shift > 25:
                shift -= 26
        buffer += en.char_encode(i, shift)
    print(buffer)

def decrypt_ui(shift, change):
    print("What is the message thet you want to decrypt")
    message = input()
    buffer = ""
    for i in message:
        if regEx.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", i) == True:
            shift += change
            if shift > 25:
                shift -= 26
        buffer += dec.decryption(shift, i)
    print(buffer)
            
main()