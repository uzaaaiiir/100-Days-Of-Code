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

def encode(plainText, key):
    '''(str,number)->str
    Given a plain text and key, the function encrypts the plaintext.
    Encrypts by shifting the plaintext characters forward by key number.
    Returns the ciphertext.
    Preconditions: plainText is a string, key is an integer.
    '''
    pass 

def decode(cipherText, key):
    '''(str,number)->str
    Given a cipher text and key, the function decodes the cipher text.
    Encrypts by shifting the ciphertext characters backward by key number.
        If key is greater than zero, shifts the ciphertext backward.
        If the key is less than zero, shifts the ciphertext forward.
    Returns the plain text.
    Preconditions: cipherText is a string, key is an integer.
    '''

def getInput():
    '''(None)->str,str,number
    Function gets the type of encryption the user wants to do: encoding or decoding.
    Function prompts the usre for the text they want to encode or decode.
    Function prompts the user for the key by which to shift the plain text or cipher text.
    Returns the encryption type, message, and key.
    Preconditions: None
    '''
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()

print(caesar_cipher)

