from bs4 import BeautifulSoup
from urllib.request import urlopen

#if has Chinese,apply decode()

html = urlopen("http://i.baidu.com/")\
       .read().decode('utf-8')

soup = BeautifulSoup(html,features='lxml')
print(soup.prettify())
'''
all_href = soup.find_all('a')
print(all_href)
all_href = [l['href'] for  l  in all_href]
print('\n',all_href)
'''

# 匹配a标签中的各个属性值
for k in soup.find_all('a'):
    print(k['href'])#查a标签的href值
    #print(k['class'])#查a标签的class属性
    #print(k['id'])#查a标签的id值
    print(k.string)#查a标签的string


'''
    beautiful soup 将复杂html文档转换成一个复杂的树形结构，每个节点都是
    python对象，所有对象分为4种：
    1.Tag
    2.NavigableString
    3.BeautifulSoup
    4.Comment
'''

##Tag

# Tag有两个重要的属性,是name和attrs
print('\n',soup.name)#soup对象本身的name即为[document]
print(soup.head.name)

print(soup.a.attrs)#把a标签的所有属性打印为字典类型

'''
#可以对属性和内容进行修改
soup.a['href'] = "http://www.baidu.com"
print(soup.a)
#可以删除属性
del soup.a['href']
print(soup.a)
'''

## NavigableString(可遍历的字符串)
# 获取标签内部的文字
print(soup.a.string)


## BeautifulSoup
'''
    BeautifulSoup 对象表示的是一个文档的全部内容.
    大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
'''

## Comment
'''
    Comment 对象是一个特殊类型的 NavigableString 对象，
    其实输出的内容仍然不包括注释符号
'''

##print(html)





















