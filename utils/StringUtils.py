# 字符串处理


class StringUtils(object):

    # 首字母大写
    @staticmethod
    def upInitials(param=''):
        return param and param.title()

    # 去掉首尾不需要的字符，默认空格，可指定字符
    @staticmethod
    def stripStr(param, sub=' ', left=0, right=0):
        if left:
            return param.lstrip(sub)
        elif right:
            return param.rstrip(sub)

        return param.strip(sub)

    # 字符串转字节
    @staticmethod
    def toByte(param):
        return bytes(param, encoding='utf-8')

    # 转字符串
    @staticmethod
    def toStr(param):
        return str(param)

    # 只有数字
    @staticmethod
    def onlyDigit(param):
        return param and param.isdigit()

    # 只有字母或文字
    @staticmethod
    def onlyAlpha(param):
        return param and param.isalpha()

    # 以指定字符开头，当substr是''时永远返回True
    @staticmethod
    def startswithStr(param, substr):
        return param and param.startswith(substr)

    # 以指定字符结尾，当substr是''时永远返回True
    @staticmethod
    def endswithStr(param, substr):
        return param and param.endswith(substr)

    # 根据英文字母表比较内容，1大于-1小于0等于
    @staticmethod
    def compareStr(str1, str2):
        if str1 == str2:
            return 0

        return 1 if str1 > str2 else -1

    # 比较是否是同一对象
    @staticmethod
    def fromSameObject(str1, str2):
        return str1 is str2

    '''
    拆分字符串: 根据分隔符将字符串分割成列表，若不传参(str.split())则包括空格，多个空格，换行符等
    split第二个参数是一个数字，表示拆分次数默认缺省，表示全分隔
    位置传参str.split(' ', 3)，指定传参str.split(maxsplit=3)
    '''
    @staticmethod
    def splitStr(param):
        return param and param.split(' ')

    # 根据字符串列表创建字符串，join前的连接符可以自定义，如逗号连接','.join()
    @staticmethod
    def mergeStr(lst):
        return ' '.join(lst)

    # 字符串的字节个数，数字/字母/小数点/下划线/空格都是一字节，汉字2-4个（取决编码方式）
    # gbk一个汉字2个字节，utf-8一个汉字3个字节
    @staticmethod
    def byteSize(param):
        return len(param.encode('utf-8'))
