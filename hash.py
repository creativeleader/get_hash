#-*- coding: ms949 -*-

import hashlib

# 일방향 알고리즘
# [공통]
def MD5(plaintext):
    hashed = hashlib.md5(plaintext.encode())
    return hashed
    
def SHA1(plaintext):
    hashed = hashlib.sha1(plaintext.encode())
    return hashed

def SHA224(plaintext):
    hashed = hashlib.sha224(plaintext.encode())
    return hashed

def SHA256(plaintext):
    hashed = hashlib.sha256(plaintext.encode())
    return hashed

def SHA384(plaintext):
    hashed = hashlib.sha384(plaintext.encode())
    return hashed

def SHA512(plaintext):
    hashed = hashlib.sha512(plaintext.encode())
    return hashed

# [일본, 유럽]
def RIPEMD160(plaintext):
    hashed = hashlib.new('ripemd160', plaintext.encode())
    return hashed

# [유럽]
def WHIRLPOOL(plaintext):
    hashed = hashlib.new('whirlpool', plaintext.encode())
    return hashed

# [한국] :: 구현 필요
"""
def HAS160(plaintext):
    hashed = hashlib.new('HAS160', plaintext.encode())
    return hashed
"""

def hashing():
    plaintext = input("# 평문입력 : ")
    
    print('[공통 : MD5, SHA1~512]')
    md5 = MD5(plaintext)
    print('MD5    hashed: {0}'.format(md5.hexdigest()))
    sha1 = SHA1(plaintext)
    print('SHA1   hashed: {0}'.format(sha1.hexdigest()))
    sha224 = SHA224(plaintext)
    print('SHA224 hashed: {0}'.format(sha224.hexdigest()))
    sha256 = SHA256(plaintext)
    print('SHA256 hashed: {0}'.format(sha256.hexdigest()))
    sha384 = SHA384(plaintext)
    print('SHA384 hashed: {0}'.format(sha384.hexdigest()))    
    sha512 = SHA512(plaintext)
    print('SHA256 hashed: {0}'.format(sha512.hexdigest()))
    
    print('')
    print('[일본, 유럽 : RIPEMD160]')
    rip160 = RIPEMD160(plaintext)
    print('RIPEMD160 hashed: {0}'.format(rip160.hexdigest()))    

    print('')
    print('[유럽 : Whirlpool]')
    whir = WHIRLPOOL(plaintext)
    print('RIPEMD160 hashed: {0}'.format(whir.hexdigest()))

    """ # 구현 필요
    print('')
    print('[한국 : HAS-160]')
    has160 = HAS160(plaintext)
    print('RIPEMD160 hashed: {0}'.format(has160.hexdigest()))
    """