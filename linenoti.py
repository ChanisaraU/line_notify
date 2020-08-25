import requests

url = 'https://notify-api.line.me/api/notify'
token = 'JLjfe9dfRrLJsu9rqRTimoQffQbBCZz6NNVHAVxA6Yu'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ส่งข้อความ LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})

print(r.content)

