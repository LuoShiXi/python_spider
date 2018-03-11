from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
#把要解析的字符串以标准的缩进格式输出

##嵌套选择soup.head.title
print(soup.head.title.name)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
'''
这里需要注意的是，有的返回结果是字符串，
有的返回结果是字符串组成的列表。
比如，name属性的值是唯一的，
返回的结果就是单个字符串。
而对于class，一个节点元素可能有多个class，所以返回的是列表。在实际处理过程中，我们要注意判断类型。
'''
print(soup.p.string)

##关联选择

#1.子节点和子孙节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
## contents属性得到直接子节点
print(soup.p.contents)

#还可以调用children属性得到相同结果
print(soup.p.children)
#children属性返回结果是生成器类型，可用for循环输出其内容
for i,child in enumerate(soup.p.children):
    print(i,child)
#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），
#enumerate（列举）将其组成一个索引序列，利用它可以同时获得索引和值

##descendants（后代）属性可以获得 所有 子、孙节点
##descendants会递归查询所有子节点，得到所有的子孙节点    

print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)

##2.父节点parent和祖先节点parents
print(soup.a.parent)

##3.兄弟节点
'''
next_sibling和previous_sibling
分别获取节点的下一个和上一个兄弟元素，
next_siblings和previous_siblings
则分别返回所有前面和后面的兄弟节点的生成器
'''
print("Next sibling:",soup.a.next_sibling.next_sibling.string)
