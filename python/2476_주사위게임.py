# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

# N(2 ≤ N ≤ 1,000)명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.

n = int(input())

nSum = list()

def isEqual(a, b, c) :
    if a == b :
        return a
    elif b == c :
        return b
    else :
        return c
    
def maxCalc(a, b, c) :
    arr = [a, b, c]
    return max(arr)

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c :
        nSum.append(10000 + a * 1000) 
    elif a == b or b == c or a == c :
        nSum.append(1000 + isEqual(a, b, c) * 100)
    else :
        nSum.append(maxCalc(a, b, c) * 100)

print(max(nSum))