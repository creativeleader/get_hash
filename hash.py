#-*- coding: ms949 -*-

import hashlib

# 일방향 알고리즘

def MD5(plaintext):
    m = hashlib.md5()
    print('ddddd', m)
    """
    m.update(plaintext)
    return m.hexdigest()
    """
"""
def SHA1(plaintext):
    return 0

def SHA224(plaintext):
    return 0

def SHA256(plaintext):
    return 0

def SHA384(plaintext):
    return 0

def SHA512(plaintext):
    return 0
"""

def hashing():
    plaintext = input("# 평문입력 : ")
    
    md5 = MD5(plaintext)
    """
    sha1 = SHA1(plaintext)
    sha224 = SHA224(plaintext)
    sha256 = SHA256(plaintext)
    sha384 = SHA384(plaintext)
    sha512 = SHA512(plaintext)
    """
    print ('[md5]: ', md5)
    """
    print ('[sha1]: ', sha1)
    print ('[sha224]: ', sha224)
    print ('[sha256]: ', sha256)
    print ('[sha384]: ', sha384)
    print ('[sha512]: ', sha512)
    """