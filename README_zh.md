# JSON 字串更新工具
若您想閱讀英文版本，請改閱讀 README.md。

歡迎改善翻譯、文件與程式！您可以閱讀「怎麽貢獻翻譯？」得知貢獻方法。

## 用法
```
用法：main.py (原始語言檔案) (翻譯語言檔案) [合併後檔案位置]
[合併後語言檔案] 非必需，未設定則只輸出比較結果。
() 代表必須、[] 代表選用
```

舉個例子：

`main.py lang/zh_TW.json lang/en_US.json lang/new.json`

其將比較 lang/zh_TW.json 與 lang/en_US.json，並以翻譯語言檔案為基準，並且複製一份 en_US.json 到 new.json。

若 zh_TW.json 有 ABC 字串，但 en_US.json 沒有，則其將會複製 ABC 字串到 new.json，並顯示出比較結果。

若 en_US.json 有 BCD 字串，但 zh_TW.json 沒有，則其將會從 new.json 中移除 BCD 字串，並顯示出比較結果。

`main.py lang/zh_TW.json lang/en_US.json`

其將比較 lang/zh_TW.json 與 lang/en_US.json，並以翻譯語言檔案為基準。

若 zh_TW.json 有 ABC 字串，但 en_US.json 沒有，則其將顯示出比較結果，但 **不修改任何檔案** 。

若 en_US.json 有 BCD 字串，但 zh_TW.json 沒有，則其將顯示出比較結果，但仍然 **不修改任何檔案** 。

## 進階使用
### 怎麽翻譯？
1. 前往 lang 資料夾，並複製 zh_TW.json (或 en_US.json，但作者英文很爛，不推薦這麼做) 至您的語言，例如 zh_CN.json
2. 開啟語言檔案並翻譯。
3. 回到本程式的根目錄開啟 settings.py，並修改 "langFile" 至您語言檔案的檔案名稱。
4. 完成！

### 怎麽合併語言檔案至最新狀態？
只需在您的終端器上輸入 `main.py lang/zh_TW.json lang/(您的語言檔案的檔案名稱) lang/(您的語言檔案的檔案名稱).new`

且移除您的 (您的語言檔案的檔案名稱)，並重新命名 (您的語言檔案的檔案名稱).new 到 (您的語言檔案的檔案名稱)

就可以翻譯了！您可以閱讀「怎麽翻譯？」來得知怎麽翻譯這個程式

### 如何貢獻翻譯？
1. 分支此程式的 master 分支
2. 上傳您的語言檔案至 lang 資料夾
3. 建立 Pull Request！（分支：master）

## 作者
pan93412 \<<pan93412@gmail.com>\>, 2018.