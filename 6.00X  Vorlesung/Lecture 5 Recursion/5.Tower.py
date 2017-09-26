def Move(fr,to):
    print('move from ' +str(fr) + ' to '+str(to))

def Towers(n,fr,to,spare):
    if n == 1:
        Move(fr,to)#只有一个盘子，打印，从from 到 to 点
    else:
        Towers(n-1,fr,spare,to) #剩下的n-1个盘子，跑到剩余地方
        Towers(1,fr,to,spare)   #最下面的一个盘子，跑到空闲地方
        Towers(n-1,spare,to,fr) #让剩下的盘子都跑到一个盘子的上面

