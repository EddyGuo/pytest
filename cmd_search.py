import webbrowser
import sys
import pyperclip

search_address = 'https://www.baidu.com/baidu?wd='
if len(sys.argv) > 1:
    # 将得到的参数连接成一个字符串，空格为间隔
    for val in sys.argv:
        if val == '--google':
            search_address = 'https://www.google.com/search?q='
        if val == '--baidu':
            search_address = 'https://www.baidu.com/baidu?wd='

    # 从参数中删除搜索引擎
    sys.argv = list(filter(lambda x: x != '--google', sys.argv))
    print('argv = ', sys.argv)
    sys.argv = list(filter(lambda y: y != '--baidu', sys.argv))
    print('argv = ', sys.argv)
    question = ' '.join(sys.argv[1:])
else:
    # 读取剪切板
    question = pyperclip.paste()

web_address = search_address + question
webbrowser.open(web_address)
print('search address = ', web_address)
