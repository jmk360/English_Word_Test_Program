import os
import time
from random import randint, shuffle

eng = [] # 영단어
kor = [] # 뜻
wrong_words = [] # 틀린 영단어
number = 10 # 문제수
cnt = 0 # 정답수
t = 0 # 시간

def read_data():
    path = os.getcwd()
    with open(path+'/wordList.txt', 'r') as f:
        data = f.readlines()
        shuffle(data)
        for line in data:
            ll = line.strip().split(' ', 2)
            eng.append(ll[1])
            kor.append(ll[2])

def test():
    global t, cnt
    start = time.time()
    print('='*50)
    print('\t{:13s}뜻'.format('영단어'))
    print('='*50)
    for i in range(number):
        if input('\t{:16s}'.format(eng[i])) == kor[i]:
            cnt += 1
        else:
            wrong_words.append(eng[i])
    print('='*50)
    end = time.time()
    t = end - start

def output_data():
    print('시간 : {:.2f}초'.format(t))
    print('맞은 개수 : {}개'.format(cnt))
    print('틀린 영단어 목록 : {}'.format(wrong_words))
    print('='*50)
    print('수고하셨습니다!!')

if __name__ == '__main__':
    read_data()
    test()
    output_data()