#(復習問題)選手6人の身長の平均が知りたい
height = [170,182,175,175,186,185]


L = [['長友','japan',170],['本田','japan',182],['香川','japan',175],['ネイマール','Brasil',175],
              ['カカ','Brasil',186],['ロナウド','portugal',185]]
#1.リストLの名前のリストを作る
>>> ['長友', '本田', '香川', 'ネイマール', 'カカ', 'ロナウド']

#2.リストLの国のリストを作る(重複不可)
>>>['japan', 'Brasil', 'portugal']

#3.リストLの身長だけのリストを作り、平均を出す
>>>[170, 182, 175, 175, 186, 185]
>>>178

#4.辞書playerの国をカウントして出力する
player = {'長友':'japan','本田':'japan','香川':'japan','ネイマール':'Brasil','カカ':'Brasil','ロナウド':'portugal'}

>>>3 2 1

#4-1.fomatを使って以下の出力に変えてください
>>>日本は3人です。ブラジルは2人です。ポルトガルは1人です。

#5.リストLの選手の出身国を辞書型にしてカウントする
L = [['長友','japan',170],['本田','japan',182],['香川','japan',175],['ネイマール','Brasil',175],
              ['カカ','Brasil',186],['ロナウド','portugal',185]]
dic = {'japan':0, 'Brasil':0, 'porutugal':0}

>>>{'japan': 3, 'Brasil': 2, 'porutugal': 1}
