'''
创建
    info = {}, info = dict()
初始化
    info = {'name': 1}
    info = dict(name = 1)
    info = {}.fromkeys(['name', 'age']), {'name': None, 'age': None}
    info = dict().fromkeys(['name', 'age']), {'name': None, 'age': None}
    info = dict().fromkeys(['name', 'age'], 1), {'name': 1, 'age': 1}
访问键值
    info['name'], 这种方式在key不存在时会触发KeyError异常，所以推荐使用get
    更优雅，info.get(name), 不存在时指定默认值info.get(name, 0)
更新键值
    info['name'] = 100, info['id'] = 01
    info.update({'name': 100, 'id': '01'}), 无返回值，即返回None
    更优雅，info.update(name=100, age=10), 无返回值
删除键值
    del info['name']
    更优雅，info.pop('name'), 返回删除的值，不存在时指定默认值info.pop('name', 0)，返回指定的默认值

常用函数
    len(dict)
    str(dict) 返回字符串形式的dict
    keys() 返回迭代器dict_keys
        返回dict的所有key，使用就需要转为list, list(dict.keys())
    values() 返回迭代器dict_values
        返回dict的所有value, 使用就需要转为list, list(dict.values())
    items() 返回键值对的元组数组dict_items
    clear() 无返回值
        清空字典({})
    copy() 返回复制后的新dict
        注意！深拷贝一级目录，子目录还是引用，会随着子目录变化
    popitem() 删除最后一对键值对，元组形势返回
        dict为空就报错

注意
    迭代dict，结果顺序和存放顺序不一定相同

技巧
    判断key是否在字典中用in，不用has_key()
'''


info = dict().fromkeys(['name', 'age'], 1)
a = info.update({'name': 100, 'id': '01'})
print(info.keys())
print(info.values())
for key, value in info.items():
    print('{0}, {1}'.format(key, value))
