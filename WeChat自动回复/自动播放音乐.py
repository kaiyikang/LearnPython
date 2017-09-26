import itchat
import os

from NetEaseMusicApi import interact_select_song


with open('stop.mp3','w') as f:
    pass

def close_music():
    os.startfile('stop.mp3')

@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    if msg['Text'] == 'schliessen':
        close_music()
        itchat.send('Musik hat geschlossen','filehelper')
    if msg['Text'] == 'helfen':
        itchat.send('Info bei Helfen','filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')

itchat.auto_login(True)
itchat.send(' ', 'filehelper')
itchat.run()