import  itchat
import time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐!'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    print(SINCERE_WISH % (friend['DispalyName'] or
          friend['NickName']), friend['UserName']
          )
    time.sleep(.5)