#201910046 김소정 hw8.py
def buy(shopping_bag):
    while True:
        print("[구입]")
        item=input("상품명? ")
        if item=='':
            return False
        number=int(input("수량은? "))
        shopping_bag[item]=number

        print(f'장바구니에 {item} {number}개 담겼습니다.')
        print()

def show(shopping_bag):
    print()
    print(f'>>> 장바구니 보기: {shopping_bag}')
    print()

def find(shopping_bag):
    print("[검색]")
    name=input("장바구니에서 확인하고자 하는 상품은? ")
    if name not in shopping_bag:
        print(f'장바구니에 {name}은(는) 없습니다.')
    else:
        print(f'{name}(는) {shopping_bag[name]}개 담겨 있습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)