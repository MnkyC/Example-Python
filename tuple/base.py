'''
索引从0开始
类似list, 但元素不能修改和删除(所以也就没有append等函数操作)，元组可以用'+'进行连接组合
del tup，删除整个元组（not defined，注意不是()或None）
可以用'*'进行复制
切片操作和list一样

转tuple
    tuple(iterable), 对于dict只保留key

注意
    连接操作后，原tuple中的元素id不变
'''

tup = ()
tup = (1,)
