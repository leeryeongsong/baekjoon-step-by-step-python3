# https://www.acmicpc.net/problem/2941

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()

for i in croatia:
    words = words.replace(i,'*')

print(len(words))


"""
# 시행착오1
# 예제 입력3에서 틀림.
# nljj에서 lj를 없애면 nj가 남는데, nj가 또 크로아티아 알파벳으로 인식된다.

words = input()
count = 0


count += words.count('c=')
words = words.replace('c=','')

count += words.count('c-')
words = words.replace('c-','')

count += words.count('dz=')
words = words.replace('dz=','')

count += words.count('d-')
words = words.replace('d-','')

count += words.count('lj')
words = words.replace('lj','')

count += words.count('nj')
words = words.replace('nj','')

count += words.count('s=')
words = words.replace('s=','')

count += words.count('z=')
words = words.replace('z=','')

count += len(words)

print(count)


"""
