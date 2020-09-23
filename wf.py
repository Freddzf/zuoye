# coding=utf-8
import os
import sys, getopt




def deal_Redundantwords(string):
    string = string.replace('\n', ' ').replace(',', ' ')
    s1 = list(string)
    num = len(s1)
    s1.append(' ')
    for i in range(num):
        if s1[i] in '."?\')-(;#$%&*!':
            if str(s1[i - 1].isalnum()) == 'True' and (str(s1[i + 1].isalnum()) == 'True'):
                pass
            else:
                s1[i] = ' '
    for i in range(num):
        if s1[i] in ':':
            if s1[i + 1] == '/':
                pass
            else:
                s1[i] = ' '
    s = ''.join(s1)
    return s


# 功能1：
def countNumber(text, flag):
    text = text.replace('\r', ' ').replace(' ', ' ').replace('.', ' ').replace(',', ' ').replace('"', ' ')
    text = deal_Redundantwords(text)
    list1 = text.replace('\n', ' ').lower().split()  # 保存原始数据
    list2 = list(set(list1))  # 去重之后的数据
    if (flag == 0):
        print("total  " + str(len(list2)))  # 小文本统计词汇量（功能1不输出words）
    else:
        print("total  " + str(len(list2)) + "  words")  # 统计词汇量
    print("\n")
    dir_a = {}  # 计算频数
    for str1 in list1:
        if str1 != ' ':
            if str1 in dir_a.keys():
                dir_a[str1] = dir_a[str1] + 1
            else:
                dir_a[str1] = 1
    dir_b = sorted((dir_a).items(), key=lambda x: x[1], reverse=True)  # 按照频数排序
    if (l > 30):
        count = 10
    else:
        count = l
    for x in range(0, count):
        print('%-10s %-10s' % (dir_b[x][0], dir_b[x][1]))  # 美化输出频数？
   


# 功能2：
def countFileWords(filename, flag):
    try:
        with open(filename, 'r', encoding='UTF-8') as f_obj:
            content = f_obj.read()
            countNumber(content, flag)
    except FileNotFoundError:
        msg = "sorry,the file " + filename + " does not exist."
        print(msg)

# 功能3：批量统计
def getdocument(folderName):
    flag = 1
    pathCurrent = os.path.abspath('.')
    pathCurrent = pathCurrent.replace('\\', '/') + '/' + folderName + '/'
    path = os.listdir(os.getcwd()) 
    folderList = []
    for p in path:
        if os.path.isdir(p): 
            folderList.append(p)

    textFolder = folderName
    fileNameList = []
    for folder in folderList:
        if textFolder == folder:
            path1 = os.listdir(folder)  # 该文件夹下所有文件建成列表
            for i in path1:
                if os.path.splitext(i)[1] == '.txt':
                    fileNameList.append(os.path.splitext(i)[0])
    for filenames in fileNameList:
        fileName = filenames + ".txt"
        path = pathCurrent + fileName
        print(filenames)
        countFileWords(path, flag)
        print("----")

# 功能4：
def main(argv):
    if sys.argv[1] == '-h':
        print('test.py -i -s filename.txt')
        sys.exit()
    elif sys.argv[1] == "-s":
        if (len(sys.argv) == 3):
            flag = 0
            countFileWords(sys.argv[2], flag)
        else:
            redirect_words = sys.stdin.read()  # 存储文件名调用方法即可
            flag = 0
            countNumber(redirect_words, flag)
    elif str(os.path.exists(sys.argv[1])) == 'True':
        getdocument(sys.argv[1])
    else:
        inputfile = sys.argv[1] + '.txt'
        flag = 1
        countFileWords(inputfile, flag)


if __name__ == "__main__":
    main(sys.argv[1:])

