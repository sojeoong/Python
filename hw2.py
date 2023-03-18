def exchange(num):
    num500 = num//500
    num=num%500
    num100 = num//100
    num=num%100
    num50=num//50
    num=num%50
    num10=num//10
    print('500원 동전의 개수:', num500)
    print('100원 동전의 개수:', num100)
    print('50원 동전의 개수:', num50)
    print('10원 동전의 개수:', num10)
    

def get_integer():
    n = int(input('동전으로 교환하고자 하는 금액은? '))
    return n


number = get_integer()
exchange(number)
