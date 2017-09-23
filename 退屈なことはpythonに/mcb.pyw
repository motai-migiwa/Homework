#! /usr/bin/env python3
# mcb.pyw クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword>　クリップボードをキーワードに紐づけて保存
# py.exe mcb.pyw  <keyword>　キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list　全キーワードをクリップボードにコピー

import shelve,pyperclip,sys #①

mcb_shelf = shelve.open('mcb') #②

#クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': #③
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

    #キーワード一覧と、内容の書き込み
    if sys.argv[1].lower() == 'list': #④
        pyperclip(str(list(mcb_shelf.keys()))) #⑤
    elif sys.argv[1] in mcb_shelf:
        pyper_clip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
