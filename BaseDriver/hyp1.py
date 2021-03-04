#@project:  ayla_ui_project
#@author: heyeping
#@file: hyp1.py
#@ide: PyCharm
#@time: 2021/3/2 2:41 PM

#利用python循环，输出1+11+111+1111+11111的值
def test1(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += int(i*"1")
    return sum1
#1 = 10**0
#11 = 10**1 + 10**0
#111 = 10**2 + 10**1 + 10**0
def test2(n):
    sum2 = 0
    for i in range(1, n+1):
        while i>0:
            sum2 += 10**(i-1)
            i -= 1
    return sum2

if __name__ == "__main__":
    print(test1(5))
    print(test2(5))
