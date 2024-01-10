import jsonpath
import json
import urllib.request


url = 'https://dianying.taobao.com/showAction.json?_ksTS=1704871787534_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true'

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Cookie': 'cna=BIjuGlDw+CACAXd7IamVieu1; miid=735296858881180679; enc=p96rK%2FyEz%2Fq3nmxuHINs1u2JBKIPSNtmWgV6n4A724%2BpVyEMrP8dj8YGkKNld7ZZjF0aWB6DUJoXEqJootQBlb7ZKZUSjo5MWa5inrGCypimqOyiHO2Mb%2BfurqRxisaR; sgcookie=E100NTEMOOw3Dd%2FPhNNYCaQcPY5vF8wcT7hak%2F1nqn9daUR2kVvGJDC80XuNMYBKNU8d8Bx8Qqc%2BeG%2FVJlIWuiA50jyHNJ39mmXSPZevn7Kc4UQ%3D; tracknick=tb287441214; _cc_=VT5L2FSpdA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _ga=GA1.2.1562895716.1679468535; _ga_YFVFB9JLVB=GS1.1.1679468535.1.1.1679468552.0.0.0; t=bd22335ac2d485127ba41d3124ee8cf7; thw=cn; _uetvid=7a2aabe0c87f11ed9636814480c17774; l=fBMOc7trLFZUnHyZBOfaPurza779_IRYmuPzaNbMi9fPOkfB5vhCW1eJs886CnGVFs9vR3utAYh6BeYBq3K-nxvOvhLyCCHmnmOk-Wf..; cookie2=1f84ba5d69a5d3ab056c50904f54fdc9; v=0; _tb_token_=e37a35567475e; xlly_s=1; isg=BAoK4i00W9v2qdCOXrfibJy0W_Cs-45VJwGU65RAUt3oR6sBfIq6ZQFxV7Obtwbt; tfstk=ePWMABxBO1RsqkM5vNp_dmEZnVFpCV9XrZHvkKL4Te8CHGF1D-yc-aOqH599iKbeJOLOXdycia_okIWvktm1KaDxBPN10xvv3zU8e8IsfK94yI5TmjS6R4VRV8eRfGo9buIUel1xOTjYslak5V6zjQLo4Xw0Z3UqHEjw-YjCKhoHl8TE3UW9bCXVbeVL99xMsUSP8XlzdiHXYoBEGjOwAHYJ6aSiru8FhSq3xbN6_HtTytEngmOwA3PLxkcScC-Bv0C..',
    'Pragma': 'no-cache',
    'Referer': 'https://dianying.taobao.com/index.htm?n_s=new',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'

}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

# print(content)

with open('淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('淘票票.json','r',encoding='utf-8'))
data = jsonpath.jsonpath(obj,'$..*')
print(data)