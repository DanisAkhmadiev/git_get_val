def get_val(collection, key, default='git'):
    '''Функция возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается значение default'''
    for i in collection:
        if i == key:
            return collection[i]
    else:
        return default