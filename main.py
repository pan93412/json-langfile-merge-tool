#!/usr/bin/env python3
'''
JSON 語言檔案字串更新工具
The string updater of JSON language file.

若您的 json 語言檔案與 VS Code 之格式相同，
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

def differ(original, translated):
    '''
    The function will diff original language file &
    translated language file, and if the function find
    the different, it will return the "different" dict.
    '''

    merged = translated.copy()

    for i in original:
        if i not in translated:
            print(i18n.str("tranNoThisString"))
            print(i18n.str("stringID") + i)
            print(i18n.str("stringContent") + original[i] + "\n")
            merged.update({i: original[i]})
        else:
            continue
    
    for i in translated:
        if i not in original:
            print(i18n.str("stringRemovedInOriginal"))
            print(i18n.str("stringID") + i)
            print(i18n.str("stringContent") + translated[i] + "\n")
            merged.pop(i)

    return merged

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print(i18n.str("usage"))
else:
    print(i18n.str("welcomeMsg"))
    # 設定指令列參數
    origFile = sys.argv[1]
    tranFile = sys.argv[2]
    if len(sys.argv) == 4:
        mergeFile = sys.argv[3]
        autoMerge = True
    else:
        autoMerge = False
    # 開啟檔案與解析 JSON
    origRaw = open(origFile, "r")
    tranRaw = open(tranFile, "r")
    origJSON = json.loads(origRaw.read())
    tranJSON = json.loads(tranRaw.read())
    origRaw.close()
    tranRaw.close()

    # 比較內容
    mergedDict = differ(origJSON, tranJSON)

    # 儲存合併檔案到 mergeFile 中
    if autoMerge == False:
        print(i18n.str("notAutoMerge")) # 若未指定第四個指令列項目
        pass
    else:
        with open(mergeFile, "w", encoding="UTF-8") as m:
            m.write(json.dumps(mergedDict, ensure_ascii=False, indent=4))
            m.flush()
        print(i18n.str("autoAddNotify") + mergeFile) # 通知

    exit()
