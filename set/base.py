'''
无序的不重复序列
可用{value1, value2...}或者set(iterable)创建，但空集合必须用set()创建
注意
    {value1, value2...}根据参数顺序创建，set方式创建的顺序不固定
    若参数有重复元素会自动去重，去重后顺序也是不固定的
    iterable是dict时只保留key

集合运算
    set1 - set2, 集合set1包含而集合set2不包含的元素
    set1 | set2, 集合set1或set2包含的所有元素
    set1 & set2, 集合set1和set2都包含的元素
    set1 ^ set2, 集合set1和set2不同时包含的元素

    注意
        运算结果是乱序的，不按照set1和set2的顺序

常用函数
    len(set)
    add(x) 无返回值
        添加元素，已存在不进行任何操作
    update(x) 无返回值
        添加元素，可以是str/list/tuple/dict
        注意！update({str})是添加str这个整体，update(str)会将str拆分成字符进行添加
    remove(x) 无返回值
        删除元素，不存在则抛异常
    discard(x) 无返回值
        移除元素，不存在不会报错
    pop() 返回删除元素
        随机删除一个元素
        注意！对于str和dict是随机的，对于list和tuple是固定第一个元素
    clear() 无返回值
        清空集合(set())
    copy() 无返回值
        复制集合

    difference(dict) 返回新集合
        集合set1包含而集合set2不包含的元素
    difference_update(dict) 无返回值
        对原dict进行修改，移除相同元素
    intersection(set2, set3...) 返回新集合
        集合set1和set2以及更多set都包含的元素
    intersection_update(set2, set3...) 无返回值
        对原dict进行修改，移除不重复的元素
    union(set2, set3...) 返回新集合
        集合set1和set2都包含的元素
    symmetric_difference(dict) 返回新集合
        集合set1和set2不同时包含的元素
    symmetric_difference_update(dict) 无返回值
        对原dict进行修改，移除目标dict中相同的元素，将不同的添加到原dict

转set
    set(iterable), 对于list和tuple会去掉重复元素，并且进行升序排序
'''
