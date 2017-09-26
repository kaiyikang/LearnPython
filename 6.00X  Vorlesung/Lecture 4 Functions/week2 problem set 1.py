s = 'aabobbobobiqwwqqwqwqwq'
count = 0
'''
这里是为了找到bob，这个字串，如果只是用s.count的话，bobob只能够识别出1个bob，而如果使用s[i:i+3]则可以找到所有的bob
'''
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print(count)
print(s.count('bob'))

'''
找到符合字母表的字段
'''

