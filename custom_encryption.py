# Alphabet used to encrypt and decrypt ------------------------------------------------------
numdict = {'a': 0, 'b': 1, 'c': 2, "d": 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}
alphadict = {0:'a', 1:'b',2:'c', 3:'d', 4:'e',5:'f',6:'g', 7:'h',8:'i',9:'j', 10:'k',11:'l',12:'m', 13:'n',14:'o',15:'p',
             16:'q',17:'r',18:'s', 19:'t',20:'u',21:'v', 22:'w',23:'x',24:'y', 25:'z'}
#---------------------------------------------------------------------------------------------

def seperate(word):     # a function that turns its input into a list of everything in the input
    result = []       # this function does not have anything to do with the encryption logic
    for l in word:    # it's just used to turn a word into a list of every letter in it , etc.
        result.append(l)
    return result
def len_alpha(text):   # this counts the length of text excluding numbers
    result = []
    for l in text:
        if l.isalpha() is True or l == " ":
            result.append(l)
    return (len(result))
def calc_mono(text):# calculates the product of the number of letters in each word e.g hi boss = 2*4
    words = text.split()
    z = 1
    for x in (words):
        y = len_alpha(x)
        g = z * y
        z = g
    return z

# The goal of this encryption method is to encrypt AND decrypt without the use of a key (an array of values used to shift each letter) because that would be too unfair
# All values used in this algorithm are derived from the input, and the alphabet used will be given to challenger. (Because Unicode would unnecassarily difficult.
# Instead of a key, the algorithm chooses a placeholder in the word based on the (calc_mono modulo number of characters) this ensures that the number chosen as key is within the word
# for example "hello world", the key is chosen by (calc_mono() modulo number of characters including spaces). So thats 5(hello) * 5(world) modulo 11(len("hello world")) = 25 mod 11 = 3
# so three is the key

def encrypt():
    text = str(input("Please enter message(only consisting of letters in alphabet) to be encrypted.\n>>\t")).lower()
    text_list = seperate(text)

    #------------distinct features-------------------------------------------------------------------
    char_num = len_alpha(text)         #number of things
    monoliew = calc_mono(text)         #Multiplication Of Number Of Letter In Each Word

    key = monoliew % char_num         
    lkey = text_list[key]
    vkey = numdict[lkey]

    for x in range(len(text_list)):
        if x == key or text_list[x] == " ":
            pass
        else:
            try:
                temp = numdict[text_list[x]]
                temp = (temp + (vkey * x)) % len(alphadict)
                eletter = alphadict[temp]
                text_list[x] = eletter
            except KeyError:
                pass

    print("".join(text_list))
encrypt()
def decrypt():
    text = str(input("\nPlease enter message(only consisting of letters in alphabet) to be decrypted.\n>>\t"))
    text_list = seperate(text)
    char_num = len_alpha(text)  # number of things
    monoliew = calc_mono(text)  # Multiplication Of Number Of Letter In Each Word

    key = monoliew % char_num
    lkey = text_list[key]
    vkey = numdict[lkey]
    for x in range(len(text_list)):
        if x == key or text_list[x] == " ":
            pass
        else:
            try:
                temp = numdict[text_list[x]]
                temp = (temp - (vkey * x)) % len(alphadict)
                eletter = alphadict[temp]
                text_list[x] = eletter
            except KeyError:
                pass
    print("".join(text_list))
decrypt()
inpu = input()
