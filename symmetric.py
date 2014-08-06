#-*- coding: ms949 -*-

# pycrypto-2.6.1 설치해야 가능
from Crypto.Cipher import AES
from Crypto import Random

# [공통]
def AES128_Encrypt():
    aes128 = 0
    return aes128 

def AES128_Decrypt():
    aes128 = 0
    return aes128 

def AES192_Encrypt():
    aes192 = 0
    return aes192 

def AES192_Decrypt():
    aes192 = 0
    return aes192 

def AES256_Encrypt():
    aes256 = 0
    return aes256 

def AES256_Decrypt():
    aes256 = 0
    return aes256

def TDEA_Encrypt():
    tdea = 0
    return tdea 

def TDEA_Decrypt():
    tdea = 0
    return tdea


# [일본]


# [유럽]


# [한국]


# symmetric_encrypt

def encrypt():
    print('test')
    # AES
    '''
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
    
    print (msg)
    '''
# symmetric_decrypt
def decrypt():
    print('')