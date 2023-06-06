# 课程链接：https://www.bilibili.com/video/BV1r8411o7EH

"""
案例实现流程：
    思路分析
    https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2174878.txt?_=1686070956374
    二,代码实现
    1,发送请求
    2.获取数据
    3.解析数据
    4.保存数据
"""
import requests
import json
url = 'https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2174878.txt?_=1686070956374'

# 1. 发送请求
response = requests.get(url=url)
# 2. 获取数据
# .text: 获取文本数据
# .json(): 获取数据以后，将字符串数据转换为json类型
# .content：获取二进制数据

# 方法一
json_data = response.text
#查看变量类型
print(type(json_data))
# 转换可直接取值为json格式
json_data = json.loads(json_data)
print(json_data['data'])

# 方法二
json_data = response.json()
print(type(json_data))