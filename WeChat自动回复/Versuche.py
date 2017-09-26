import itchat
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    whoSendMe = itchat.get_friends(update=True)[0]["UserName"]
    if whoSendMe:
        itchat.send('test',whoSendMe)


itchat.auto_login(True)
itchat.run()
