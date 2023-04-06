#201910046 지적재산권학과 김소정

def read_single_digit(n):
    if n==1:
        return '일'
    elif n==2:
        return '이'
    elif n==3:
        return '삼'
    elif n==4:
        return '사'
    elif n==5:
        return '오'
    elif n==6:
        return '육'
    elif n==7:
        return '칠'
    elif n==8:
        return '팔'
    elif n==9:
        return '구'

def read_number(num):
    if num/100!=0:
        a = read_single_digit(num//100)
    if num/10!=0:
        b=read_single_digit(num//10 - num//100*10)
    if 0<=num%10<=9:
        c=read_single_digit(num%10)
    sp=' '
    ch=a+sp+b+sp+c
    return ch

number=int(input("세 자리 정수 입력: "))
ch=read_number(number)
print(ch)