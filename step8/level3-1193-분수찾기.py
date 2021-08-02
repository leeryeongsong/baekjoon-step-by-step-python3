# https://www.acmicpc.net/problem/1193

X = int(input())

end_num = 1
gap = 1
count = 1

while end_num<X:
    count += 1
    gap += 1
    end_num += gap

order = X - (end_num - gap) -1
if count % 2 == 0:
    print(f"{1+order}/{count-order}")
else:
    print(f"{count-order}/{1+order}")
