# simple-discordWebhook-sender
Send message to your server with Webhook sender!

# 사용법
```python
from Simplesender import Simplesender

content = input() # 보낼 메시지
a = Simplesender.sender('웹훅주소', content, '웹훅 이름')
a.sends() # 
```

반복해서 쓰고싶으면 while문 추가가능
```python

from Simplesender import Simplesender

while True:
    content = input() # 보낼 메시지
    a = Simplesender.sender('웹훅주소', content, '웹훅 이름')
    a.sends() # 
```
