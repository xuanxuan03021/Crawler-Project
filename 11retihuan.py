import re

string='''i love you,you love me'''
pattern=re.compile(r'love')#多行匹配
#方法一
# ret=pattern.sub('hate',string)#找全部的是FINDAL，只找第一个是search
# print(ret)
#方法二
ret=re.sub(pattern,'hate',string)
print(ret)
#函数写在前面

def fn(a):
    ret=int(a.group(0))
    print(ret)
    return str(ret-10)
#将180改成180-10，（在他的的基础上减10）
string1='我喜欢180的男士'
pattern=re.compile(r'\d+')
ret=pattern.sub(fn,string1)# 调用的时候，可以不传参数
print(ret)


