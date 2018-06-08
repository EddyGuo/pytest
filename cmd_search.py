import webbrowser
import sys
import pyperclip
import search_func as sf


searchers = ['google', 'bing', 'baidu']
if len(sys.argv) > 1:
    # 选择搜索引擎
    search_address = sf.address_searcher(sys.argv)

    # 从参数中删除搜索引擎
    sys.argv = sf.del_searcher(searchers, sys.argv)

    # 将得到的参数连接成一个字符串，空格为间隔
    question = ' '.join(sys.argv[1:])
else:
    # 读取剪切板
    question = pyperclip.paste()

web_address = search_address + question
webbrowser.open(web_address)
print('search address = ', web_address)
