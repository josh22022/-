'''
Case : 計算重複字母
ID : 407180221
'''
print("Calculating times of letters that appears more than two.")
letters=" "+"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
characters=input("Please input a line of characters or numbers :")
print("========")
print("Letters : Appear times [Position]")


for i in letters:
    index = []
    number = 0
    for j in range(0,len(characters)):
        if i == characters[j:j+1]:
            index.append(j+1)
            number += 1 
    if number >= 2:
        print(i,":",len(index),index)
 
