import shutil
from modules.getFileList import getFileNameList
from modules.makeFolder import makeFolder
from modules.showMessage import showMessage

# ターゲットフォルダを指定
_dir = input("処理したいフォルダパスを入力:")
files = []
folderM = f"{_dir}/M"
folderL = f"{_dir}/L"
folderMask = f"{_dir}/Mask"

getFileNameList(_dir, files)
makeFolder(folderM, folderL, folderMask)

@showMessage
def main():
    for file in files:
        match file:
            case _ if file.endswith(".MOS"):
                shutil.move(f'{_dir}/{file}', f'{folderMask}/{file}')
            case _ if file.endswith("M.png") or file.endswith("M.PNG"):
                shutil.move(f'{_dir}/{file}', f'{folderM}/{file}')
            case _ if file.endswith("L.png") or file.endswith("L.PNG"):
                shutil.move(f'{_dir}/{file}', f'{folderL}/{file}')

if __name__ == "__main__":
    main()