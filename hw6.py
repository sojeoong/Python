#201910046 지적재산권학과 김소정

for i in range(2,10,4):
    for j in range(1,10,1):
        print(f'{i} x {j} = {i*j:2d}', end='   ')
        print(f'{i+1} x {j} = {(i+1)*j:2d}', end='   ')
        print(f'{i+2} x {j} = {(i+2)*j:2d}', end='   ')
        print(f'{i+3} x {j} = {(i+3)*j:2d}')

    print()    
        
