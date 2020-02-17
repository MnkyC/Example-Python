'''
索引从0开始
常用函数
    len(lst)
    append(obj) 无返回值
        list末尾添加一个对象。注意！若改变obj中的值，list中的对应元素也会改变
    extend(seq) 无返回值
        list末尾追加另一序列(list/tuple/set/dict, 若为dict仅将key作为元素添加)，seq改变不影响list
    pop([index=-1]) 返回移除元素，默认移除最后一个元素
        index为索引，可选，但不能超过list长度（pop index out od range）
    insert(index, ob) 无返回值
        在list指定位置插入对象
    remove(obj) 无返回值
        移除list中第一个匹配项
    clear() 无返回值
        清空列表（[]），类似于del lst[:]
    sort(key=None, reverse=False) 无返回值
        对list进行排序，reverse默认升序，key是指定的比较函数，可以用lambda，如比较长度lambda item:len(item)
    copy() 返回复制后的新list
        复制list，类似于lst[:]，新list和原list互不影响
    reverse() 无返回值
        反向list中的元素
    index(obj[, start[, end]]) 返回第一个匹配项的索引位置，没有就抛异常
        start和end是索引起始位置和结束位置，可选
    count(obj) 返回元素出现次数
        某个元素在list中出现几次

    注意
        对于层叠列表，如[[0,1], [1,2], [2,3]]，insert和append操作后，obj修改后会对list产生影响
        增删操作后，list剩下元素的id不变
        sort操作不能用于int和str混合比较，汉字和英文字母同时存在会优先对字母进行排序

转list
    list(tuple), 对于dict只保留key

切片
    lst[:], 复制
    lst[:3]/lst[0:3], 前三个元素
    lst[10:20], 区间[10,19]
    lst[:10:2], 前10个元素，第一个位置开始，每间隔1个元素取一个
    lst[::5], 每间隔4个元素取一个
    lst[-2:], 倒数两个元素
    lst[-2:-1], 倒数第二个元素
'''

info = [item * 2 for item in range(10)]
info = [i for i in range(1, 10)]
