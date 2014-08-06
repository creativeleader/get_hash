#-*- coding: ms949 -*-

import hash, symmetric

def main_interface():
    print ('### 대칭키/일방향/인코딩 ###')
    print ('1. 대칭키(Symmetric key)')
    print ('2. 일방향(Hash)')
    print ('3. 인코딩(Encode)')
    print ('========================')
    select = input("# 숫자를 입력하세요 : ")
    return select

# Symmetric Interface
def Sym_interface():
    print ('### 대칭키(암호화/복호화) ###')
    print ('1. 암호화(Encrypt)')
    print ('2. 복호화(Decrypt)' )
    print ('========================')
    select = input("# 숫자를 입력하세요 : ")
    return select

# Hash Interface
"""
def Hash_interface():
    print ('### 일방향  ###')
    print ('1. 일방향(Hash)')
    print ('========================')
    select = input("# 숫자를 입력하세요 : ")
    return select
"""

# Encode Interface
def Encode_interface():
    print ('### 인코딩/디코딩  ###')
    print ('1. 인코딩(Encode)')
    print ('2. 디코딩(Decode)')
    print ('========================')
    select = input("# 숫자를 입력하세요 : ")
    return select

def main():
    # 리턴값이 문자로 옮
    sel_1 = int(main_interface())
    # print('sel_1 : ', sel_1)
    # 대칭키
    if sel_1 == 1:  
        print ('')
        sel_2 = int(Sym_interface())
        if sel_2 == 1:
            print ('')
            print ('## 대칭키 암호화 ##')
        elif sel_2 == 2:
            print ('')
            print ('## 대칭키 복호화 ##')

    # 일방향
    elif sel_1 == 2:
        print ('')
        print ('## 일방향 알고리즘 ##')
        hash.hashing()
                        
    # 인코딩/디코딩
    elif sel_1 == 3:
        print ('')
        sel_2 = int(Encode_interface())
        if sel_2 == 1:
            print ('')
            print ('## 인코딩 ##')
        elif sel_2 == 2:
            print ('')
            print ('## 디코딩 ##')
            

if __name__ == "__main__":
    main()