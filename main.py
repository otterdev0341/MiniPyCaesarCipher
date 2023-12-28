from CaesarCipher import *
def main():
    sentenceToEncode: str = "Cat is cute but Otter cutie"
    rotary_num: int = 1_111_111
    
    encrypeMessage = getEncryptMessage(sentenceToEncode,rotary_num)
    decrypeMessage = getDecryptMessage(encrypeMessage,rotary_num)

    print(f"Original message is {sentenceToEncode}")
    print(f"Encrypt message is : {encrypeMessage}")
    print("=================")
    print(f"Decrypt message is {decrypeMessage}")

if __name__=='__main__':
    main()