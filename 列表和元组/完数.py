# 打表

'''
n = int(input())

if n == 1:
    print("6=1+2+3")
elif n == 2:
    print("""6=1+2+3\n28=1+2+4+7+14""")
elif n == 3:
    print("""6=1+2+3\n28=1+2+4+7+14\n496=1+2+4+8+16+31+62+124+248""")
elif n == 4:
    print("""6=1+2+3\n28=1+2+4+7+14\n496=1+2+4+8+16+31+62+124+248\n8128=1+2+4+8+16+32+64+127+254+508+1016+2032+4064""")
elif n == 5:
    print("""6=1+2+3\n28=1+2+4+7+14\n496=1+2+4+8+16+31+62+124+248\n8128=1+2+4+8+16+32+64+127+254+508+1016+2032+4064\n33550336=1+2+4+8+16+32+64+128+256+512+1024+2048+4096+8191+16382+32764+65528+131056+262112+524224+1048448+2096896+4193792+8387584+16775168""")
elif n == 6:
    print("""6=1+2+3\n28=1+2+4+7+14\n496=1+2+4+8+16+31+62+124+248\n8128=1+2+4+8+16+32+64+127+254+508+1016+2032+4064\n33550336=1+2+4+8+16+32+64+128+256+512+1024+2048+4096+8191+16382+32764+65528+131056+262112+524224+1048448+2096896+4193792+8387584+16775168\n8589869056=1+2+4+8+16+32+64+128+256+512+1024+2048+4096+8192+16384+32768+65536+131071+262142+524284+1048568+2097136+4194272+8388544+16777088+33554176+67108352+134216704+268433408+536866816+1073733632+2147467264+4294934528""")

'''

'''
import math
n = int(input())

def find(n):
    count = 1
    for i in range(2305843008139952128, 2305843008139952129, 2):
        sum = 0
        ls = []
        j = 1
        if str(i)[-1] == '6' or str(i)[-1] == '8': 
            if count == 0: break
            while j <= i // 2:
                if i % j == 0:
                    sum += j
                    ls.append(j)
                j += 1
            if sum == i:
                printAns(sum, ls)
                count -= 1

def printAns(i, ls):
    print(i, end='')
    print('=',end='')
    print('+'.join(map(str,ls)))

find(n)
'''