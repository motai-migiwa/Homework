#! /usr/bin/env python3
# backupToZip.py フォルダ全体を連番付きZIPファイルにコピーする

import zipfile,os #①

def backup_to_zip(folder):
    #フォルダ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder) #folderを絶対パスにする

    #既存のファイル名からファイル名の連番を決める
    number = 1  #②
    while True: #③
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if # NOTE: os.path.exists(zip_filename):
            break
        number = number + 1

    # TODO: ZIPファイルを作成する ④
    print('Creating {}...'.format(zip_filename))
    backup_zip = zip_file.ZipFile(zip_filename,'w') #①


    # TODO: フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.work(folder): #①
    print('Adding files in {}...'.format(foldername))

    #現在のフォルダをZIPに追加する
    backup_zip.write(foldername) #②

    #現在のフォルダの中の全ファイルをZIPファイルに追加する
    for filename in foldernames: #③
        new_base = os.path.basename(folder) + '_'
        if filename.startswith(new_base) and filename.endswith('.zip'):
                continue #バックアップ用ZIPファイルはバックアップしない
        backup_zip.close()
        print('Done.')

backup_to_zip('')
