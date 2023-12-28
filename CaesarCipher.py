# Function Idea
# create 2 list : 1 is a-z, 2 is A-Z in ASCII CODE
# take rotary_num, then extend 2 list to support all range of ratary_num
# create list to collect result
# create  3 function, 1 for upper, 1 for lower, 1 for non-alphabet check by ASCII CODE
# append those ASCII CODE to list
# convert list of ASCII CODE to str then return

#info : with lotary_num = 7_777_777 the code exec in 2.882 seconds.
#critical : with lotary_num = 88_888_888 the code exec in 34.837 seconds. <!--Big-O critical problem-->
#critical : with lotary_num = 88_888_888 can consume 34 GB memory to exec !!!!!
#critical : with positive Integer 2_147_483_647 by man Integer this function still can't handle.

def getEncryptMessage(message: str, lotary_num: int):
    # list to collect each alphabet that encrypt
    encryptMessage: str = []
    preEncryptMessage: int = []
    resultEncryptMessage: str = ""

    #Init list depend on lotary_num
    lowerAlphabet: int = []
    upperAlphabet: int = []
    for i in range(0,26):
        lowerAlphabet.append(97+i)
        upperAlphabet.append(65+i)
    # + 1 to make sure length of alphabet can loop for
    lowerAlphabet = lowerAlphabet * (lotary_num + 1)
    upperAlphabet = upperAlphabet * (lotary_num + 1)
    
    for c in message:
        slug = getSlug(ord(c))
        match slug:
            case "lowerCase":
                index: int = lowerAlphabet.index(ord(c)) + lotary_num
                preEncryptMessage.append(lowerAlphabet[index])
            case "upperCase":
                index: int = upperAlphabet.index(ord(c)) + lotary_num
                preEncryptMessage.append(upperAlphabet[index])
            case "noneAlphabet":
                preEncryptMessage.append(ord(c))
            case _:
                print("not matching any case")
    for asc in preEncryptMessage:
        encryptMessage.append(chr(asc))
    resultEncryptMessage ="".join(encryptMessage)

    return resultEncryptMessage

def getDecryptMessage(message: str, lotary_num: int):
    # list to collect each alphabet that encrypt
    decryptMessage: str = []
    preDecryptMessage: int = []
    resultDencryptMessage: str = ""

    #Init list depend on lotary_num
    lowerAlphabet: int = []
    upperAlphabet: int = []
    for i in range(0,26):
        lowerAlphabet.append(97+i)
        upperAlphabet.append(65+i)
    # + 1 to make sure length of alphabet can loop for
    lowerAlphabet = lowerAlphabet * (lotary_num + 1)
    upperAlphabet = upperAlphabet * (lotary_num + 1)
    
    for c in message:
        slug = getSlug(ord(c))
        match slug:
            case "lowerCase":
                index: int = lowerAlphabet.index(ord(c)) - lotary_num
                preDecryptMessage.append(lowerAlphabet[index])
            case "upperCase":
                index: int = upperAlphabet.index(ord(c)) - lotary_num
                preDecryptMessage.append(upperAlphabet[index])
            case "noneAlphabet":
                preDecryptMessage.append(ord(c))
            case _:
                print("not matching any case")
    for asc in preDecryptMessage:
        decryptMessage.append(chr(asc))
    resultDencryptMessage ="".join(decryptMessage)

    return resultDencryptMessage

# for make code more easily to work with
#use this method to defind which case that we need to handle
def getSlug(ascii_code:int):
    slug: str = ""
    if ascii_code >= 97 and ascii_code <=122:
        slug = "lowerCase"
    elif ascii_code >= 65 and ascii_code <= 90:
        slug = "upperCase"
    else:
        slug = "noneAlphabet"
    return slug

