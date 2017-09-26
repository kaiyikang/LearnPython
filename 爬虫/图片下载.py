import urllib.request
import os
import time
os.chdir('D:\\')
os.getcwd()

for i in range(1,10,1):
    name = 'D:\\00'+ str(i)+'.jpg'
    url = 'http://web3.cartoonmad.com/c86ns736r62/1698/232/00'+ str(i)+'.jpg'
    req = urllib.request.urlopen(url)
    f = open(name,'wb')
    f.write(req.read())
    f.close()
    print(str(i)+ 'downloaded!' )
    time.sleep(8)



