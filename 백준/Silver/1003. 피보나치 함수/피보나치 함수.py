def fibo_cnt(number):
    zero = [1, 0, 1] 
    one = [0, 1, 1]
    if number >= 3:
        for i in range(3, number + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f'{zero[number]} {one[number]}')    
    
n = int(input())
for _ in range(n):
    fibo_cnt(number=int(input()))
