import os

def getFileNameList(target_folder, file_list):
    files = os.listdir(target_folder)
    for _, f in enumerate(files):
        file_path = os.path.join(target_folder, f)
        # ファイルかどうかを判断
        if os.path.isfile(file_path):
            file_list.append(f)