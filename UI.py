#-*- coding: ms949 -*-

import hash, symmetric

def main_interface():
    print ('### ��ĪŰ/�Ϲ���/���ڵ� ###')
    print ('1. ��ĪŰ(Symmetric key)')
    print ('2. �Ϲ���(Hash)')
    print ('3. ���ڵ�(Encode)')
    print ('========================')
    select = input("# ���ڸ� �Է��ϼ��� : ")
    return select

# Symmetric Interface
def Sym_interface():
    print ('### ��ĪŰ(��ȣȭ/��ȣȭ) ###')
    print ('1. ��ȣȭ(Encrypt)')
    print ('2. ��ȣȭ(Decrypt)' )
    print ('========================')
    select = input("# ���ڸ� �Է��ϼ��� : ")
    return select

# Hash Interface
"""
def Hash_interface():
    print ('### �Ϲ���  ###')
    print ('1. �Ϲ���(Hash)')
    print ('========================')
    select = input("# ���ڸ� �Է��ϼ��� : ")
    return select
"""

# Encode Interface
def Encode_interface():
    print ('### ���ڵ�/���ڵ�  ###')
    print ('1. ���ڵ�(Encode)')
    print ('2. ���ڵ�(Decode)')
    print ('========================')
    select = input("# ���ڸ� �Է��ϼ��� : ")
    return select

def main():
    # ���ϰ��� ���ڷ� ��
    sel_1 = int(main_interface())
    # print('sel_1 : ', sel_1)
    # ��ĪŰ
    if sel_1 == 1:  
        print ('')
        sel_2 = int(Sym_interface())
        if sel_2 == 1:
            print ('')
            print ('## ��ĪŰ ��ȣȭ ##')
        elif sel_2 == 2:
            print ('')
            print ('## ��ĪŰ ��ȣȭ ##')

    # �Ϲ���
    elif sel_1 == 2:
        print ('')
        print ('## �Ϲ��� �˰��� ##')
        hash.hashing()
                        
    # ���ڵ�/���ڵ�
    elif sel_1 == 3:
        print ('')
        sel_2 = int(Encode_interface())
        if sel_2 == 1:
            print ('')
            print ('## ���ڵ� ##')
        elif sel_2 == 2:
            print ('')
            print ('## ���ڵ� ##')
            

if __name__ == "__main__":
    main()