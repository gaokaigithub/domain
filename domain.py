import requests
from bs4 import BeautifulSoup
import time

#查询是否注册
def check(domain):
    url = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"%domain
    html = requests.get(url)
    bsj = BeautifulSoup(html.text,"lxml")
    onum = bsj.find("original")
    if onum != None:
        num = onum.get_text()[:3]
        if num == '210':
            print("%s可以注册"%domain)
        elif num == "213":
            print("查询超时，请重新查询")
        elif num == "211":
            print("%s域名已注册"%domain)
        else:
            print("出现未知问题")
        return num
    else:
        print("让我哭一会，ip可能被封了")
        return None

def domainlist(namepart):
    # 获取单词列表
    text = []
    with open('word.txt', 'r') as w:
        words = w.readlines()
    for word in words:
        text.append(word.strip())
    # 生成域名列表
    names = []
    for word in text:
        name1 = namepart+word
        name2 = word+namepart
        names.append(name1)
        names.append(name2)
    return names

#保存可注册域名
def domain(namepart,suffix):
    oklist = []
    names = domainlist(namepart)
    for name in names:
        domain = name+'.'+suffix
        time.sleep(1)
        num = check(domain)
        if num != None:
            if num == '210':
                oklist.append(domain)
        else:
            break
    with open('oklist.txt','w+') as ok:
        for k in oklist:
            s = k+'\n'
            ok.write(s)
    return oklist

if __name__ == '__main__':
    namepart = input('输入要查询的主题：')
    suffix = input('输入域名后缀: ')
    oklist = domain(namepart,suffix)