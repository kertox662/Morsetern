letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

morseCode = ['12','2111','2121','211','1','1121','221','1111','11','1222','212','1211','22','21','222','1221','2212','121','111','2','112','1112','122','2112','2122','2211']

def wordToTern(word):
    code = []
    for i in word:
        index = letters.index(i.lower())
        code.append(morseCode[index])
    
    code = "0".join(code)

    return int(code)

def ternToWord(tern):
    word = str(tern).split("0")

    for i in range(len(word)):
        word[i] = letters[morseCode.index(word[i])]
    
    word = "".join(word)

    return word

def ternToDec(tern):
    dec = list(str(tern))
    dec.reverse()
    decNum = 0
    for i in range(len(dec)):
        decNum += int(dec[i]) * 3 ** i

    return decNum

def decToTern(dec):
    ternNum = []
    while dec > 0:
        r = dec % 3
        ternNum.append(str(r))
        q = dec // 3
        dec = q
    
    ternNum = "".join(reversed(ternNum))
    return int(ternNum)

def encodeWord(word):
    tern = wordToTern(word)
    code = ternToDec(tern)
    return code

def decodeWord(code):
    tern = decToTern(code)
    word = ternToWord(tern)
    return word

def quadToDec(quad):
    dec = list(str(quad))
    dec.reverse()
    decNum = 0
    for i in range(len(dec)):
        decNum += int(dec[i]) * 4 ** i

    return decNum

def decToQuad(dec):
    ternNum = []
    dec = int(dec)
    while dec > 0:
        r = dec % 4
        ternNum.append(str(r))
        q = dec // 4
        dec = q
    
    ternNum = "".join(reversed(ternNum))
    return int(ternNum)

def encodeSentence(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = str(wordToTern(words[i]))
    
    quad = int("3".join(words))
    code = quadToDec(quad)

    return code

def decodeSentence(code):
    quad = decToQuad(code)
    words = str(quad).split("3")
    for i in range(len(words)):
        words[i] = ternToWord(int(words[i]))
    
    sentence = " ".join(words)

    return sentence


while True:
    process = input("Encode or Decode?")
    if process in ["encode", "Encode"]:
        sentence = input("Type the sentence to encode:")
        print(encodeSentence(sentence))
    elif process in ["decode", "Decode"]:
        sentence = input("Type the sentence to decode:")
        print(decodeSentence(sentence))
    
    else:
        print("Could not recognize process, try again.")
    
    print()