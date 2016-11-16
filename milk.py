import socket
import re

#目前添加了com,net,cn,cc,me后缀的whois查询

class mywhois():
    hostdict = {'com': 'whois.internic.net',
                'me': 'whois.nic.me', 'cn': 'whois.cnnic.cn',
                'cc': 'whois.nic.cc', 'net': 'whois.internic.net'}
    fword = {'com':'No match','me':'NOT FOUND','cc':'No match','net':'No match','cn':'No matching record'}
    #获取whois
    def get_whois(self,name,suffix):
        domain = name+'.'+suffix
        host = self.hostdict[suffix]
        s = socket.socket()
        s.connect((host,43))
        s.send(domain.encode('idna') + b"\r\n")
        v = s.recv(4096).decode()
        return v

    #提取asd返回的相关信息的字典
    def extract(self,name,suffix):
        info = self.get_whois(name,suffix)
        whois = {}
        whois['domain_name'] = re.search('Domain Name:(.*)',info).group(1).lower()
        whois['creation_date'] = re.search('Creation Date:(.*)|Registration Time:(.*)',info).group(1).lower()
        whois['expiration_date'] = re.search('Expiration Date:(.*)|Registry Expiry Date:(.*)|Registration Time:(.*)',info)
        return whois

    #判断是否可注册
    def ornot(self,name,suffix):
        info = self.get_whois(name,suffix)
        num = info.find(self.fword[suffix])
        domain = name+'.'+suffix
        if num>=0:print('%s可注册'%domain)
        else:print('%s已被注册'%domain)
        return num








