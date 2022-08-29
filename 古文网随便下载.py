# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,sys
url=input('输入章节网址：')
html=requests.get(url)
Myhtml=html.text.encode('iso-8859-1').decode('gbk')
bs=BeautifulSoup(Myhtml,'lxml')
txt=bs.find_all('div',class_='zhangjie')
txt1=BeautifulSoup(str(txt[0]),'lxml')
txt2=txt1.find_all('a')
nums=len(txt2[:])
for each in txt2:
    hrefurl='https://www.gdwxcn.com'+each.get('href')
    href=requests.get(hrefurl).text.encode('iso-8859-1').decode('gbk')
    bs1=BeautifulSoup(href,'lxml')
    txt3=bs1.find_all('div',class_='xstext')
    txt4=txt3[0].text.replace('  ','\n\n')
    path='L:\九月\\'+each.string+'.txt'   
    sys.stdout.write('正在下载'+each.string+'\r')
    sys.stdout.flush()
    #print(txt4)
    with open(path,'w') as f:
        f.write(each.string+'\n')
        f.writelines(txt4)
        f.write('\n\n')      
print('下载完成！')
    #print(each.string,each.get('href'))
