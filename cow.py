from milk import mywhois

cow = mywhois()
#获取域名列表
def domainlist(namepart,num):
    # 获取单词列表
    text = []
    with open('word.txt', 'r') as w:
        words = w.readlines()
    for word in words:
        text.append(word.strip())
    # 生成域名列表
    names = []
    if len(namepart) == 0:
        names = [word for word in text]
    else:
        for word in text:
            if num == 1:
                name1 = namepart + word
                names.append(name1)
            elif num == 2:
                name2 = word + namepart
                names.append(name2)
            elif num == 0:
                name1 = namepart+word
                name2 = word+namepart
                names.append(name1)
                names.append(name2)
    return names

#保存可注册域名
def domain(namepart,suffix,num = 1):
    oklist = []
    names = domainlist(namepart,num)
    for name in names:
        domain = name+'.'+suffix
        num = cow.ornot(name,suffix)
        if num != None:
            if num>=0:
                oklist.append(domain)
        else:
            break
    with open('oklist.txt','w+') as ok:
        for k in oklist:
            s = k+'\n'
            ok.write(s)
    return oklist

if __name__ == '__main__':
    print('查询模式:1代表主题+单词,2代表单词+主题,0代表两种都查')
    namepart = input('输入要查询的主题：')
    suffix = input('输入域名后缀: ')
    num = int(input('输入查询模式：'))
    oklist = domain(namepart,suffix)