from urllib.parse import urlencode
import requests
import json

#base_url用来表示请求的URL的前半部分
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'authority':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/1105032440',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '1105032440',
        'containerid':'1076031105032440',
        'page':page
    }
    ##对containerid的解释：主页的containerid是100505加博主ID，微博内容的是107603加博主ID
    
    #调用urlencode()方法将参数转化为URL的GET请求参数格式，
    #即类似于type=uid&value=5594495993&containerid=1076035594495993&page=2这样的形式
    url = base_url + urlencode(params)
    try:
        response = requests.post(url,headers=headers)
        if response.status_code == 200:
            #print(response.text)
            return(response.json())
    except requests.ConnectionError as e:
        print('Error',e.args)

##定义一个解析方法，从结果中提取想要的信息
#分析可知：先遍历cards,然后获取mblog中的各个信息，赋值为一个新的字典
from pyquery import PyQuery as pq

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        #print(json['data'].get('cards'))
        for item in items:
            weibo = {}
            data=item['mblog']
            weibo['id'] = data.get('id')
            weibo['created_time']=data.get('created_at')
            #借助pyquery将正文中的HTML标签去掉
            weibo['text'] = pq(data.get('text')).text()
            weibo['attitudes'] = data.get('attitudes_count')
            weibo['comments'] = data.get('comments_count')
            weibo['reposts'] = data.get('reposts_count')
            yield weibo

#最后遍历page,一共10页，将提取结果打印输出
if __name__=='__main__':
    for page in range(1,10):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            #print('Page:',page)
            print(result)

###提示：parse_page()函数中包含迭代器yield，
### 所以parse_page()函数应该用在for循环中使用，
### 否则返回<generator object parse_page at 0x066F31E0>
