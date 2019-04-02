# -*- coding: utf-8 -*- 
import requests
import time
from bs4 import BeautifulSoup

# 准备cookie用于登录
# 可以在Chrome等浏览器手动登录后获取cookie, 根据对应字段修改下面的值即可
timestamp = '%d'%(int(time.time()))
cookie = {
    'Hm_lvt_375aa6d601368176e50751c1c6bf0e82': '[此处需要修改]',
    'Hm_lpvt_375aa6d601368176e50751c1c6bf0e82': timestamp,
    'sessionid': '[此处需要修改]',
    'csrftoken': '[此处需要修改]'
}

# 登录url
check_url = 'http://readfree.me/accounts/checkin'

# 将签到结果推送到手机的Bark app(可选功能)
# 如果你的Bark app里显示的推送链接是 https://api.day.app/abcdefg/这里改成你自己的推送内容
# push_url 就设置为'https://api.day.app/abcdefg/'
# 推送的内容由后面的message变量提供

#push_url = '[此处需要修改Bark推送链接]'

message=''

# 登录
res = requests.get(check_url,cookies=cookie)

if res.status_code == 200:

    # 找到最新一条签到记录
    confirm_url = 'https://readfree.me/accounts/profile/[此处需要修改为你的readfree用户名]/checkin/'
    re = requests.get(confirm_url, cookies=cookie)
    soup = BeautifulSoup(re.text, features="html.parser")
    latest_time = soup.find('tr', class_='info').td
    latest_score = latest_time.find_next() #最后一次签到获得的积分
    total_score = latest_score.find_next() #最后一次签到后的总积分

    # 检查它的日期是不是今天
    date = time.strftime("%Y-%m-%d", time.localtime())
    if latest_time.text.startswith(date):
        message = '本次签到获得' + latest_score.text[1:] + '个积分，累计积分：' + total_score

    else:
        message = '签到失败，可能是cookie过期了'

else:
    message = '无法访问readfree.me'

print(message)

# 将结果推送的Bark app(可选功能)
#requests.post(push_url+message)
