'''
Unicode编码的字符组成的不可变序列，不支持对其中单个字符的任何操作，如append, clear, pop等
也不支持删除del str，因为str只是引用，不会导致字符串对象的消亡
转字符串: str(number/bool/list/tuple/dict)
转数字: int(str)
'''

# %d整数，%f浮点数，%x16进制数，%s字符串
print('%s %s' % ('Hello', 'Python'))

# format拼接，py2.6引入
print('Hello {}'.format('Python'))
print('Hello {0}'.format('Python'))
print('Hello {name}'.format(name='Python'))

# ()类似元组方式，元素都是真实字符串，不能使用变量
print(('Hello' ' ' 'Python'))

# +号拼接，当拼接的最终字符串长度不超过20时比join快，与+号使用次数无关，因为常数折叠，编译器会完成拼接，运行期不变
print('Hello ' + 'Python')

# join拼接，拼接长度超过20时首选
print(' '.join(['Hello', 'Python']))

# f-string，py3.6引入，可读性比format好，处理长字符串时速度与join相当
name = 'Python'
print(f'Hello {name}')

# 总结：字符串列表等序列结构用join，拼接长度<=20用+号，>20时高版本用f-string，低版本用format或join
# 注意!!!复杂场景下，避免使用这些原生方法，应该用第三方库
