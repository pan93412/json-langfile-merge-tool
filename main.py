#!/usr/bin/env python3
'''
JSON 語言檔案字串更新工具
The string updater of JSON language file.

若您的 json 語言檔案與以下格式相同，
則您的軟體同樣也能透過這工具更新翻譯字串。

* 格式範例 Format Example
{
    "stringID1": "string1",
    "stringID2": "string2"
}
'''
import os, json, sys
from I18N import I18N
import settings as opti

i18n = I18N.I18N("lang/zh_TW.json", "lang/" + opti.langFile)

def differ(original, translated, obsolete):
    '''
    The function will diff original language file &
    translated language file, and if the function find
    the different, it will return the "different" dict.
    '''

    merged = translated.copy() # 複製 translated 這個字典的副本

    # 若 original 有某字串，但 translated 沒有某字串，則
    # 輸出檢查結果，並對 merged 字典增加 translated 缺失的項目。
    for i in original:
        if i not in translated:
            print(i18n.str("tranNoThisString"))
            print(i18n.str("stringID") + i)
            print(i18n.str("stringContent") + original[i] + "\n")
            merged.update({i: original[i]})
        else:
            continue
    
    # 若 obsolete == True，則檢查如下項目
    # 若 translated 有某字串，但 original 沒某字串，則輸出
    # 檢查結果，並對 merged 字典刪除已不存在 original 的字串項目。
    if obsolete:
        for i in translated:
            if i not in original:
                print(i18n.str("stringRemovedInOriginal"))
                print(i18n.str("stringID") + i)
                print(i18n.str("stringContent") + translated[i] + "\n")
                merged.pop(i)

    return merged

if len(sys.argv) < 3 or len(sys.argv) > 6:
    print(i18n.str("usage_0"))
    print(i18n.str("usage_1"))
    print(i18n.str("usage_2"))
    print(i18n.str("usage_3"))
    exit(1)
else:
    argv = sys.argv.copy() # 複製 sys.argv 的副本
    
    # 處理傳入引數部分。
    #
    # 正常情況下應該會有以下引數：
    # argv[0] -> 執行檔名稱
    # argv[1] -> 原始語言檔案
    # argv[2] -> 目標語言檔案
    # argv[3] -> 合併後語言檔案之儲存位置 (若沒有指定儲存位置，則應該就是 `--obsolete` 或 `--sort`)
    # argv[4] -> (maybe) `--sort` or `--obsolete`
    # argv[5] -> (maybe) `--sort` or `--obsolete`
    
    if "--obsolete" in argv: # 若 --obsolete 在引數中
        cleanObsolete = True # 設定 cleanObsolete 為真
        argv.remove("--obsolete")
    else:
        cleanObsolete = False

    if "--sort" in argv: # 若 --sort 在引數中
        sort_keys = True # 設定 sort_keys 為真
        argv.remove("--sort")
    else:
        sort_keys = False

    if len(argv) > 3:
        # --obsolete 和 --sort 從列表中刪除之後應該只會剩下 4 個引數
        # 第一個引數為執行檔名稱、第二、三個引數為輸入處理檔案名稱
        # 第四個引數則為合併完結果儲存位置。
        #
        # 但若去掉 --obsolete 和 --sort 只剩下三個引數，則直接跳過此處理部分
        mergeFile = argv[3]
        autoMerge = True
    else:
        autoMerge = False
        
    # 設定指令列參數
    origFile = argv[1] # 原始語言檔案
    tranFile = argv[2] # 目標語言檔案

    print(i18n.str("welcomeMsg")) # 顯示歡迎訊息
    
    # 確保 origFile 和 tranFile 存在
    if os.path.exists(origFile) and os.path.exists(tranFile):
        pass
    else:
        raise Exception(i18n.str("fileNotFound"))

    # 開啟檔案與解析 JSON
    origRaw = open(origFile, "r")
    tranRaw = open(tranFile, "r")
    
    origJSON = json.loads(origRaw.read())
    tranJSON = json.loads(tranRaw.read())
    
    origRaw.close()
    tranRaw.close()

    # 比較兩者內容
    mergedDict = differ(origJSON, tranJSON, cleanObsolete)

    # 儲存合併檔案到 mergeFile 中
    if autoMerge == False:
        print(i18n.str("notAutoMerge")) # 若未指定第四個指令列項目
        pass
    else:
        # 若 mergeFile 已經存在
        if os.path.exists(mergeFile):
            print(i18n.str("mergeFileExists"))
            exit()
        
        # 開啟 mergeFile 並寫入合併結果
        with open(mergeFile, "w", encoding="UTF-8") as m:
            m.write(json.dumps(mergedDict, ensure_ascii=False, indent=4, sort_keys=sort_keys))
            m.flush()
        
        print(i18n.str("autoAddNotify") + mergeFile) # 通知
    exit()
