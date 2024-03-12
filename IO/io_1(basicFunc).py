# open(), .read(), .seek()

file = open("myFile.txt")
# print(file.read(5))  # seek 跑到 5
# print("---------")
# file.seek(0)  # 將 seek 設定在 0
# print(file.read(5))
# hello, .read() will return a string
# ---------
# hello


# .readlines(), .readline(), .close()
# print(file.readlines())  # ['hello, how r u today?\n', "I'm fine, thanks."]
# file.seek(0)
print(file.readline())
print(file.readline())
# hello, how r u today?

# I'm fine, thanks.
