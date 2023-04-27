#연습문제 9.4
shopping_bag=[]
shopping_bag_d={}
print("[구입]")
while True:
    item=input("상품명? ")
    if item=='':
        break
    number=int(input("수량은? "))
    shopping_bag.append(item)
    shopping_bag_d[item]=number

    print(f'장바구니에 {item} {number}개 담겼습니다.')
    print()

print(f'>>>장바구니 보기:{shopping_bag_d}')
print()
print("[검색]")
p=input("장바구니에서 확인하고자 하는 상품은? ")
print(f'{p}은(는) {shopping_bag_d.get(p)}개 담겨 있습니다.')