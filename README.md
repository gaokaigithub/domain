# domain
## 1、domain.py
<h3>输入要查询的主题，如 vr，后缀，如com，然后调用万网api查询，其中word.txt使用<br>
<h3>http://xueyuan.me/topic/49/获取2000个常用单词<br>
<h3>设置了睡眠时间，但查询一定次数还是可能会被封ip。<br>

##2、milk.py
<h3> milk用来查询域名的whois信息，并判断域名是否已经注册<br>

##3、cow.py
<h3>小奶牛和domain.py是一样的程序，只不过没有调用万网api，而是使用的milk.py来判断域名是否已经注册，并添加了查询模式<br>
<h3>'1'代表主题+单词，'2'代表主题+单词，'0'两种都查。
