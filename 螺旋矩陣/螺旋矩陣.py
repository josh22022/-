"""
Case : 螺旋矩陣
ID : 407180221
"""
import numpy as np
n=eval(input('Input the size of the matrix (odd number):')) #奇方陣的階數
if (n%2) == 0:
    print("Error ! Not an odd number.")
else :
    a = np.random.randint(10, size=(n, n)) #隨機的奇方陣,element < 10
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
功能：
    判斷是否為奇數
    創建隨機方陣
    順時鐘螺旋
    逆時鐘螺旋
'''
