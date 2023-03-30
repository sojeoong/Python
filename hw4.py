#201910046 김소정

def draw_line_string(str):
    msg1=f'Hello {str},'
    msg2='Welcome to Seoul.'
    nstr=len(msg1) if(len(msg1)>len(msg2)) else len(msg2)
    
    print('-'*nstr)
    print(msg1,msg2,sep='\n')
    print('-'*nstr)

str=input('Input his/her name: ')
draw_line_string(str)
