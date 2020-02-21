'''
None, 0, [], {}, '', ""都是False
len(lst) == 0和value == True/False可以用隐式布尔条件
    if not lst:, if value/not value:, if result is None:

多个条件语句可以用set和list简化判断
    if role in ['a', 'b', 'c']

注意
    不要用==和!=比较None和布尔值，直接用隐式布尔语句，区分布尔和None可以用if value is None
    for i in range(5): print(i) i =10，i=10这条赋值语句不会影响循环

高级用法
    三目运算: (条件 and a or [b])[0]
    链式比较: 1 < i < 3, 1 < i <= 3
    [func1, fucn2](1)(), 函数对象的list，可以用index统一调用

特殊函数
    lambda函数
        不用命名，有任意数量的参数，但表达式只有一个
    map函数
        可将函数应用于各种数据结构中的元素，py2返回list，py3返回迭代器，需要用list()强转
    filter函数
        用于list/tuple/dict，返回对应函数返回True的元素，需要用list()强转
'''

multiply = lambda a, b : a * b
alg = lambda a : a * 3 + 3

def square(a):
    return a * a

def func(a, b):
    return a * b

print(list(map(lambda a : a * a, [1, 2, 3])))
print(list(map(square, [1, 2, 3])))
print(list(map(func, [1, 2, 3], [4, 5])))

def filter_odd_number(source):
    return True if source % 2 == 0 else False

print(list(filter(lambda x: x > 2, range(1, 10))))
print(list(filter(filter_odd_number, range(10))))

# itertools，处理迭代器的工具集合
import itertools

# 不用if/else实现不同计算方法, 参考策略模式
from operator import add, sub, mul, truediv, pow
def calc(a, b, opt):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
        "**": pow
    }[opt](a, b)

# 函数链
def add_or_sub(a, b, opt):
    return (add if opt == "+" else sub)(a, b)

# 第n次出现的位置
def search_n(source, target, n):
    count = 0
    for index, item in enumerate(source):
        if item == target:
            count += 1
        if count == n:
            return index
    
    return -1

'''
内置小工具
    下载服务器，默认端口8000
        python -m http.server 8080
    命令行字符串转JSON
        echo '{"job": "developer", "name": "lmx", "sex": "male"}' | python -m json.tool
    验证第三方库是否正确安装
        本地环境可以用import进行导入，远程环境可以用脚本python -c 'import xxx'
    解压zip
        linux下不支持用tar解压zip，需要用unzip但大部分没有安装unzip
        创建: python -m zipfile -c mon.zip test1.txt test2.txt
        查看: python -m zipfile -l mon.zip
        解压: python -m zipfile -e mon.zip target-dir/
'''
