import requests
import pprint
import json

def send_message(token,content,group_id):
    r=requests.request(
        method="POST",
        headers={
            "Accesstoken": token,
            "Refer":"https://www.boxim.online/",
            "Content-Type":"application/json"
        },
        data=json.dumps({
            "content": content,
            "type": 0,
            "groupId": group_id,
            "atUserIds": [],
            "receipt": False,
        }),
        url="https://www.boxim.online/api/message/group/send"
    )
    pprint.pprint(json.loads(r.content))
