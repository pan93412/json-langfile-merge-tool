# JSON String Updater
If you want to see Chinese (Traditional) version, please
read README.md instead.

Welcome to improve the translation, docs & program! You can read "How to contribute my translation?" know how to contribute.

## Usage
```
Usage: main.py (Original language file) (Translated language file) [The merged language file path]
[The merged language file path] is optional，If you don't set that, the program will just print the diff result.
() means require、[] means optional
```

For example:

`main.py lang/zh_TW.json lang/en_US.json lang/new.json`

It will diff lang/zh_TW.json & lang/en_US.json and based on the translated language file, and then clone en_US.json to new.json.

If zh_TW.json has ABC string but en_US.json doesn't, it will copy the ABC string to new.json & print the diff result.

If en_US.json has BCD string but zh_TW.json doesn't, it will remove BCD string from new.json & print the diff result.

`main.py lang/zh_TW.json lang/en_US.json`

It will diff lang/zh_TW.json & lang/en_US.json and priority to the translated language file.

If zh_TW.json has ABC string but en_US.json doesn't, it will print the diff result BUT **DOESN'T MAKE CHANGE IN ANY FILES**.

If en_US.json has BCD string but zh_TW.json doesn't, it will print the diff result BUT ALSO **DOESN'T MAKE CHANGE IN ANY FILES**.

## Advanced Usage
### How to translate?
1. Go to lang folder, and copy zh_TW.json (or en_US.json, but my English is too bad, so not recommends) to your language, ex. zh_CN.json 
2. Open your language file, and translate.
3. Go back to the program's root directory, and open settings.py, and change "langFile" to your language file's filename.
4. All done!

### How to merge translation to latest?
Just input `main.py lang/zh_TW.json lang/(your language file's filename) lang/(your language file's filename).new` on your terminal.

And remove (your language file's filename), and rename (your language file's filename).new to (your language file's filename)

You can translate it now! You can read "How to translate?" to know
how to translate the program.

### How to contribute my translation?
1. Fork the program's master branch
2. Upload your language file to "lang" folder.
3. Make a Pull Request! (Branch: master)

## Author
pan93412 \<<pan93412@gmail.com>\>, 2018.
