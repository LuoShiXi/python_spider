from bs4 import BeautifulSoup
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# find_all(name , attrs , recursive , text , **kwargs)
soup = BeautifulSoup(html,'lxml')

### 1.name
print(soup.find_all(name = 'ul'))
print(type(soup.find_all(name = 'ul')[0]))

for ul in soup.find_all(name = 'ul'):
    print(ul.find_all(name='li'))

for li in soup.find_all(name='li'):
    print(li.string)

### 2.attrs按属性查询
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
#同上，可简化操作
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
#由于class在Python里是一个关键字，所以后面需要加一个下划线，
#即class_='element'，返回的结果依然还是Tag组成的列表。

### 3.text
#text参数可用来匹配节点的文本内容，传入的形式可以是字符串，
#可以是正则表达式对象
import re

html1 = '''
<div class="link">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1,'lxml')
print(soup1.find_all(text=re.compile('link')))

### find & find_all
#除了find_all()方法，还有find()方法，
#只不过后者返回的是单个元素，也就是第一个匹配的元素，
#而前者返回的是所有匹配的元素组成的列表






















