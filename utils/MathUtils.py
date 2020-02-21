# 数学算法
from _pydecimal import Context, ROUND_HALF_UP


class MathUtils(object):

    # 绝对值
    @staticmethod
    def absValue(value):
        return abs(value)

    # 十进制转二进制
    @staticmethod
    def toBin(value):
        return bin(value)

    # 十进制转八进制
    @staticmethod
    def toOct(value):
        return oct(value)

    # 十进制转十六进制
    @staticmethod
    def toHex(value):
        return hex(value)

    # 十进制转ASCII字符，65->'A'，97->'a'
    @staticmethod
    def toASCII(value):
        return chr(value)

    # ASCII转十进制
    @staticmethod
    def fromASCII(value):
        return ord(value)

    # 次幂, z存在则需要对结果进行取模再返回(pow(x,y)%z)
    @staticmethod
    def powValue(x, y, z=None):
        return pow(x, y, z)

    # 取商和余数
    @staticmethod
    def divmodValue(value, divisor):
        return divmod(value, divisor)

    # 四舍五入
    # 精度要求不高，round(value[, n])，n表示小数点后保留的位数，默认0表示整数后加.0
    # 推荐decimal
    @staticmethod
    def roundValue(value, n=None):
        return (Context(prec=3, rounding=ROUND_HALF_UP).create_decimal(str(value)))

    # 求和, 适用于list和tuple
    @staticmethod
    def sumValues(values):
        return sum(values)

    # 去掉最高和最低求平均，借助切片操作，左闭右开
    @staticmethod
    def average_score(lst):
        lst.sort()
        lst_src = lst[1:(len(lst) - 1)]
        return round((sum(lst_src) / len(lst_src)), 2)
