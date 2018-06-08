def address_searcher(argv):
    """选择搜索引擎"""
    # 默认使用百度
    search_address = 'https://www.baidu.com/baidu?wd='
    for val in argv:
        if val == '--google':
            search_address = 'https://www.google.com/search?q='
        elif val == '--baidu':
            search_address =  'https://www.baidu.com/baidu?wd='
        elif val == '--bing':
            search_address = 'https://cn.bing.com/search?q='
    return search_address


def del_searcher(searchers, argv):
    """从参数中删除搜索引擎"""
    for searcher in searchers:
        argv = list(filter(lambda x: x != '--' + searcher, argv))
    return argv
