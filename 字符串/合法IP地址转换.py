str = input()
# 二进制转换int(a, 2)
print(int(str[0:8],2),end='.')
print(int(str[8:16],2),end='.')
print(int(str[16:24],2),end='.')
print(int(str[24:32],2),end='')