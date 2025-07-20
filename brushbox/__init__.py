import requests
import pprint
import json
from .TokenExcecpion import TokenException

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
    if json.loads(r.content)['code']==401:
        raise TokenException
