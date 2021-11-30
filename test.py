import requests 

url = ""
while True:
    i = input()
    data = {
        "content" : i,
        "username" : "test"
    }

    req = requests.post(url, json = data)

    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("전송완료, 코드 {}".format(req.status_code))
