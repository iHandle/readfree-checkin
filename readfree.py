# -*- coding: utf-8 -*- 
import requests
import time
from bs4 import BeautifulSoup

# 登录
def login(cookie):

    url = 'http://readfree.me/accounts/checkin'
    res = requests.get(url, cookies=cookie)

    if res.status_code == 200:
        return confirm(cookie)
    else:
        return '无法访问readfree.me'

# 确认是否签到成功
def confirm(cookie):

    # 找到最新一条签到记录
    url = 'https://readfree.me/accounts/profile/[此处需要修改为你的readfree用户名]/checkin/'
    res = requests.get(url, cookies=cookie)
    soup = BeautifulSoup(res.text, features="html.parser")
    latest_rec = soup.find('tr', class_='info')

    if latest_rec is None:
        return '签到失败，可能是cookie过期了'

    latest_time = latest_rec.td             # 最后一次签的时间
    latest_score = latest_time.find_next()  # 最后一次签到获得的积分
    total_score = latest_score.find_next()  # 最后一次签到后的总积分

    # 检查最后一次签到的日期是不是今天
    date = time.strftime("%Y-%m-%d", time.localtime())

    if latest_time.text.startswith(date):
        message = '本次签到获得' + latest_score.text[1:] + '个积分，累计积分：' + total_score.text
        return message

    else:
        # 不知道有没有这种情况
        return '签到失败，cookie可能没过期'



# 准备cookie用于登录
# 可以在Chrome等浏览器手动登录后获取cookie, 根据对应字段修改下面的值即可
timestamp = '%d' % (int(time.time()))
cookie = {
    'Hm_lvt_375aa6d601368176e50751c1c6bf0e82': '[此处需要修改]',
    'Hm_lpvt_375aa6d601368176e50751c1c6bf0e82': timestamp,
    'sessionid': '[此处需要修改]',
    'csrftoken': '[此处需要修改]'
}

result = login(cookie)
print(result)

## 将签到结果推送到手机的Bark app(可选功能)
## 如果你的Bark app里显示的推送链接是 https://api.day.app/abcdefg/这里改成你自己的推送内容
## push_url 就设置为'https://api.day.app/abcdefg/'

# bark_url = '[此处需要修改Bark推送链接]'
# requests.post(bark_url+result)
