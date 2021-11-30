import requests 

url = "https://discord.com/api/webhooks/909804938396323860/ERHlv2euuke_8GQHDyRb2zCDVcvdFUyWYd1pls3pN9LEtWfNVLlv86PXbK0sAisQ8F7p" 
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
