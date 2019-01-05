#!/bin/python
import re

def ip_bin(s):
    result = ''
    for i in re.split(r'[.]',s):
        if int(i) >= 0 and int(i) <= 255:
            result = result + str(bin(int(i)))[2:].zfill(8) + '.' 
        else:
            print('IP地址格式不对')
    return result[0:-1]

def s_bin(s):
    result = ''
    result = '1'*s.zfill(32)
    pattern = re.compile('.{8}')
    result = '.'.join(pattern.findall(result))
    return result

def s_mask(s):
    result = s_bin(s)
    for i in re.split(r'[.]',result):
        temp = str(int(i,2)) + '.'
    result = temp[:-1]
    return result

a = '192.168.10.10'
print(ip_bin(a))