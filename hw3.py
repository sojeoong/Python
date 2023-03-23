#201910046 김소정 hw3.py

def get_fixed_price(sale, price):
    price2=price/((100-sale)/100)
    return price2

sale = int(input("할인율은? "))
saleA = int(input('A 상품의 할인된 가격은? '))
saleB = int(input('B 상품의 할인된 가격은? '))

priceA = get_fixed_price(sale, saleA)
priceB = get_fixed_price(sale, saleB)

print('A 상품의 정가는', int(priceA),'원')
print('B 상품의 정가는', int(priceB),'원')