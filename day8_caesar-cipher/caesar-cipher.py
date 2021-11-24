caesar_cipher = '''
                                               ,d                                                             88                        
                                               88                                                             88                         
 ,adPPYba, 8b,dPPYba, 8b       d8 8b,dPPYba, MM88MMM ,adPPYba,   ,adPPYb,d8                                   88                         
a8"     "" 88P'   "Y8 `8b     d8' 88P'    "8a  88   a8"     "8a a8"    `Y88 8b,dPPYba, ,adPPYYba, 8b,dPPYba,  88,dPPYba,  8b       d8    
8b         88          `8b   d8'  88       d8  88   8b       d8 8b       88 88P'   "Y8 ""     `Y8 88P'    "8a 88P'    "8a `8b     d8'    
"8a,   ,aa 88           `8b,d8'   88b,   ,a8"  88,  "8a,   ,a8" "8a,   ,d88 88         ,adPPPPP88 88       d8 88       88  `8b   d8'     
 `"Ybbd8"' 88             Y88'    88`YbbdP"'   "Y888 `"YbbdP"'   `"YbbdP"Y8 88         88,    ,88 88b,   ,a8" 88       88   `8b,d8'      
                          d8'     88                             aa,    ,88 88         `"8bbdP"Y8 88`YbbdP"'  88       88     Y88'       
                         d8'      88                              "Y8bbdP"                       88                          d8'         
                                                                                                 88                         d8'      
'''

def strToList(str):
    '''(str)->list
    Function takes a string as input and returns a list where each element is a character from the string.
    '''
    text = []
    for i in range(len(str)):
        text.append(str[i])
    return text

def listToStr(lst):
    '''(list)->str
    Function takes a list and returns it as a concatenated string.
    '''
    s = ''
    for i in range(len(lst)):
        s = s  + lst[i]
    return s 

def encode(plainText, shift):
    '''(str,number)->str
    Given a plain text and key, the function encrypts the plaintext.
    Encrypts by shifting the plaintext characters forward by key number.
    Returns the ciphertext.
    Preconditions: plainText is a string, key is an integer.
    '''
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    plainText = strToList(plainText)
    for i in range(len(plainText)):
        if plainText[i].isupper():
            x = upperCase.index(plainText[i])
            shiftN = (shift+x)%25
            plainText[i]=upperCase[shiftN]
            shiftN = 0
        elif plainText[i].islower():
            x = lowerCase.index(plainText[i])
            shiftN = (shift+x)%25
            plainText[i]=lowerCase[shiftN]
            shiftN = 0
    cipherText = listToStr(plainText)
    return cipherText
    

def decode(cipherText, shift):
    '''(str,number)->str
    Given a cipher text and key, the function decodes the cipher text.
    Encrypts by shifting the ciphertext characters backward by key number.
        If key is greater than zero, shifts the ciphertext backward.
        If the key is less than zero, shifts the ciphertext forward.
    Returns the plain text.
    Preconditions: cipherText is a string, key is an integer.
    '''
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipherText = strToList(cipherText)
    for i in range(len(cipherText)):
        if cipherText[i].isupper():
            x = upperCase.index(cipherText[i])
            shiftN = (x-shift)%25
            cipherText[i]=upperCase[shiftN]
            shiftN = 0
        elif cipherText[i].islower():
            x = lowerCase.index(cipherText[i])
            shiftN = (x-shift)%25
            cipherText[i]=lowerCase[shiftN]
            shiftN = 0
    plainText = listToStr(cipherText)
    return plainText

print(caesar_cipher)

flag = True

while flag:
    user = input("Do you want to encrypt/decrypt a message?[yes/no] \n").lower().strip()
    print()
    if user=='yes':
        flag1=True
        while flag1:
            type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
            if type!='encode' and type!='decode':
                print("Please enter 'encode' or 'decode'.")
                print()
            elif type in ['encode', 'decode']:
                print()
                flag1=False
        text = input("Type your message:\n")
        print()
        flag2=True
        while flag2:
            try:
                shift = (int(input("Type the shift number:\n")))
                print()
                flag2=False
            except:
                print('Please enter an int.')
                print()

        if type=='encode':
            messageEncoded = encode(text,shift)
            print(f'The encoded text is {messageEncoded}')
        elif type=='decode':
            messageDecoded = decode(text,shift)
            print(f'The decoded message is {messageDecoded}')
    elif user=='no':
        print('No problem, thank you!')
        flag=False
    else: 
        print('Please enter yes or no.')
