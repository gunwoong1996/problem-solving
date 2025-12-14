k = int(input())  # 두 주사위를 굴려 나오는 합 k 

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

for i in range(6):
    for j in range(6):
        if (dice1[i] + dice2[j]) == k:
            print(dice1[i],dice2[j])
