# Author 6ViRuS
# Github : 6virus
# Cipher

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def dec():
    count = 0
    for s in range(26):
        count += 1
        def decode(text,s):
            res = ""
            textlow = text.lower()
            for letext in textlow:
                if letext == " ":
                    res += " "
                else:
                    for i in range(len(letters)):
                        if letters[i] == letext:
                            res += letters[i-s]
                            break
            return print("[!] #",count, "[ ", res, " ]")
        decode(text,count)
def enc():
    s = int(input("Shift : "))
    def encode(text,s):
        res = ""
        textlow = text.lower()
        for letext in textlow:
            if letext == " ":
                res += " "
            else:
                for i in range(len(letters)):
                    if letters[i] == letext:
                        res += letters[i-s]
                        break
        return print("Result : ", res)
    encode(text,s)

print("[1] Decode")
print("[2] Encode")
user = int(input("Choose : "))
if user == 1:
    text = str(input("Enter Text : "))
    dec()
elif user == 2:
    text = str(input("Enter Text : "))
    enc()
else:
    print("Choose one of them")
