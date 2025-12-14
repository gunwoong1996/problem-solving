n,m = map(int,input().split()) #가로길이,세로길이

for i in range(1,m+1):
    
    if i == 1 or i == m :
        print("+" + "-"*(n-2) + "+")
    if i>1 and i<m:
        print("|" + " "*(n-2) + "|")
