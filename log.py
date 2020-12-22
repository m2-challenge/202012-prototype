import os
import linecache


def saveLog(path, *data):
    with open(path, "a") as f:
        for i in range(len(data)):
            if isinstance(data[i], list):
                for j in range(len(data[i])):
                    f.write(str(data[i][j]) + "\t")
                    #print(str(data[i][j]) + "\t", end="")
            else:
                f.write(str(data[i]) + "\t")
        f.write("\n")
        # print()


def fileName(f, ext):
    i = 0
    num = ""
    while 1:
        num = ""
        if(len(str(i)) <= 4):
            for j in range(4 - len(str(i))):
                num = num + "0"
            num = num + str(i)
        else:
            num = str(i)
        if not(os.path.exists(f + num + "." + ext)):
            break
        i = i + 1
    f = f + num + "." + ext
    return f


if __name__ == "__main__":
    name = fileName("test", "txt")
    print(name)

    data = [10, 20, 30, 40, 50]
    saveLog(name, data)
