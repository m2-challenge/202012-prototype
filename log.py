import os


def saveLog(path, *data):
    """Save Log File
    （dataをpathで指定されたファイルに保存する．dataは可変長引数．それぞれの要素はタブで区切られて書込まれる）


    Args:
        path (string): file path of log
        date (list): log date
    """
    with open(path, "a") as f:
        for d in data:
            if isinstance(d, list):
                for d_ in d:
                    f.write("{}\t".format(d_))
            else:
                f.write("{}\t".format(d))
        f.write("\n")


def fileName(f, ext):
    """Create File Name
    （例：f=log_file,ext=.txtとし，ディレクトリ内に"log_file0000.txt", "log_file0001.txt"がある場合，この関数は"log_file0002.txt"）

    Args:
        f (string): file name exclude extension
        ext (string): file extension

    Returns:
        string: new file name
    """
    i = 0
    while 1:
        file_name = "{0}{1:0>4}.{2}".format(f, i, ext)
        if not os.path.exists(file_name):
            break
        i = i + 1
    return file_name


if __name__ == "__main__":
    name = fileName("test", "txt")
    print(name)

    data = [10, 20, 30, 40, 50]
    saveLog(name, data)
    data = 10
    saveLog(name, data)
