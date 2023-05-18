#hw10.py 201910046 김소정

import os
import pickle

def input_scores():
    lst=[]
    i=1
    print("[점수 입력]")
    while (True):
        n=int(input(f'#{i}? '))
        if n<0:
            break
        else:
            lst.append(n)
        i+=1
    print()
    return lst

def get_average(lst):
    sum=0
    for j in range(len(lst)):
        sum+=lst[j]
    avr=sum/len(lst)
    return avr

def show_scores(lst):
    print("[점수 출력]")
    print("개인점수: ",end="")
    for k in range(len(lst)):
        print(lst[k],end=' ')
    print()
    avr=get_average(lst)
    print(f'평균: {avr}')

def save_data(student_score, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(student_score, file)

def load_data(filepath):
    with open(filepath, 'rb') as file:
        scores=pickle.load(file)
    return scores

student_score=[]
filename="score.bin"
if os.path.exists(filename):
    print("[파일 읽기]\n")
    student_score=load_data(filename)
    show_scores(student_score)
else:
    student_score=input_scores()
    show_scores(student_score)

save_data(student_score, filename)

