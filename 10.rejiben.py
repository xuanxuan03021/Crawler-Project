import re
# string='<p><div><span>猪八戒</span></div></p>'
# pattern=re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
#
# string2='<div>猪八戒</div></div>'
# pattern2=re.compile(r'<(\w+)>.*</\1>')
# ret=pattern2.search(string2)
# print(ret)
#
#
# string2='<div>猪八戒</div></div>'
# pattern2=re.compile(r'<(\w+)>.*?</\1>')#是否加问号是有区别的
# ret=pattern2.search(string2)
# print(ret)

string2='''he is a man
love is her
love me 
love him '''
pattern2=re.compile(r'^love',re.M)#多行匹配
ret=pattern2.findall(string2)#找全部的是FINDAL，只找第一个是search
print(ret)

string3='''<div>沁园春-雪
沛国风光
千里冰封
万里雪飘
望长城内外
惟余莽莽
</div>'''
pattern3=re.compile(r'<div>(.*)</div>',re.S)
ret3=pattern3.findall(string3)#这种情况用search和search 都行
print(ret3)


