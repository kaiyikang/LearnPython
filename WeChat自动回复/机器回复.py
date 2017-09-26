import itchat
import  requests

from itchat.content import *

KEY = '1107d5601866433dba9599fac1bc0083'

#对msg进行注册
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])


# 1. 图灵对话
# 对于tuling对话的key

# tuling回复，将信息输入到对应的api，返回对应语句
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return

#进行tuling对话
def tuling_reply(msg):
    defaultReply = 'I received: '+ msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(True)
itchat.run()