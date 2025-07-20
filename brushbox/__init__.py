import requests
import pprint
import json

def send_message():
    r=requests.request(
        method="POST",
        headers={
            "Accesstoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzODIzMiIsImV4cCI6MTc1Mjk4NTI3NiwiaW5mbyI6IntcIm5pY2tOYW1lXCI6XCJ4aWFvbGU2MzI0XCIsXCJ0ZXJtaW5hbFwiOjAsXCJ1c2VySWRcIjozODIzMixcInVzZXJOYW1lXCI6XCJ4aWFvbGU2MzI0XCJ9In0.utlFCcWSAG5-nFhcA-y5BypnJgrulFejBPRPzlwQnNI",
            "Refer":"https://www.boxim.online/",
            "Content-Type":"application/json"
        },
        data=json.dumps({
            "content": "RUOK？",
            "type": 0,
            "groupId": 8152,
            "atUserIds": [],
            "receipt": False,
        }),
        url="https://www.boxim.online/api/message/group/send"
    )
    pprint.pprint(json.loads(r.content))

if __name__=="__main__":
    send_message()