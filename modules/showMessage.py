def showMessage(func):
    def func_wrapper():
        print("ファイル分類開始～")
        func()
        print("ファイル分類を成功しました")
    return func_wrapper