"""
Case : 螺旋矩陣
ID : 407180221
"""
import numpy as np
n=eval(input("Input the size of the matrix (odd number):")) 
if (n%2) == 0:
    print("Error ! Not an odd number.")
else :
    a = np.random.randint(10, size=(n, n)) 
    print("===============")
    print("Random matrix :\n",a)
    
    #順時鐘
    cntr=int((n-1)/2)
    print("===============")
    print("# Clockwise")
    print("Start at matrix center :","[",cntr+1,",",cntr+1,"]","=",a[cntr,cntr])
    print("Right , Down , Left , Up")
    for i in range(1,cntr+1):
        print(a[cntr-i+1,cntr+i],">",a[cntr+i,cntr+i],">",a[cntr+i,cntr-i],">",a[cntr-i,cntr-i])
    print("Final :","[ 1 ,",n,"] =",a[0,n-1])
    
    #逆時鐘
    print("===============")
    print("# Ct.Clockwise")
    print("Start at matrix center :","[",cntr+1,",",cntr+1,"]","=",a[cntr,cntr])
    print("Left , Down , Right , Up")
    for i in range(1,cntr+1):
        print(a[cntr-i+1,cntr-i],">",a[cntr+i,cntr-i],">",a[cntr+i,cntr+i],">",a[cntr-i,cntr+i])
    print("Final :","[ 1 , 1 ] =",a[0,0])

'''
說明：
    隨機產生奇方陣，以中心點順時鐘及逆時鐘向外旋轉，並回報路徑上的每個元素值。
功能：
    判斷是否為奇數
    創建隨機方陣
    順時鐘螺旋
    逆時鐘螺旋
思路：
    與中心點的相對位置具規律性，使用迴圈將每層四角取出。
'''
