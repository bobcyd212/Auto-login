import requests
from lxml import etree
s = requests.Session()
post_url = 'http://www.doki8.com/wp-login.php'
post_data ={
    'log':'chopper212',
    'pwd': 'jafrUh-hytgiz-dedda2',
    'captcha': '1234',
    'wp-submit': '登录',
    'redirect_to': 'http://www.doki8.com/drama',
    'testcookie': '1',
    }
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
profile_url = 'http://www.doki8.com/members/chopper212/profile/edit/group/1/'
s.post(post_url,data=post_data,headers=headers,)
r = s.get(profile_url)
print('登录成功！')
html = etree.HTML(r.text)
html_data = html.xpath('//*[@id="item-header-content"]/div[3]/text()')
print(html_data)


