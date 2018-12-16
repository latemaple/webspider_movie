import requests
#异常处理
from requests.exceptions import RequestException
#正则表达式
import re

#提取网页内容
def get_page(url):
    try:
        headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding #根据爬去内容确定字体编码
            return response.text
        return None
    except RequestException:
        return None

#解析网页内容,正则表达式
def parse_page(html):

    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?class="board-img" />.*?.*?title="(.*?)" .*?star">(.*?)</p>.*?time">(.*?)</p>',
        re.S)

#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    items = re.findall(pattern,html)
   # res=[]
    for item in items:
        content={
            'ranking':item[0],
            'picture':item[1],
            'name':item[2],
            'actors':item[3].strip(),
            'time':item[4]
        }
        print(content)
   #     res.append(content)
  #  print(res)




if __name__ == '__main__':
    for i in range(10):
        url="http://maoyan.com/board/4?offset="+str(i*10)
        html=get_page(url)
    #    print(html)
        parse_page(html)














