def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    result=radius*radius*3.14
    return result

r=get_radius("넓이를 구하고자 하는 원의 반지름은? ")
res=get_circle_area(r)
print("반지름", r,"인 원의 넓이 = 3.14 x", r, "x", r, "=", res)
