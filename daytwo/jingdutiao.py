# -*- coding:utf8 -*-
#=========知识储备==========
#进度条的效果
# [#             ]
# [##            ]
# [###           ]
# [####          ]

#指定宽度
print('[%-15s]' %'#')
print('[%-15s]' %'##')
print('[%-15s]' %'###')
print('[%-15s]' %'####')

#打印%
print('%s%%' %(100)) #第二个%号代表取消第一个%的特殊意义

#可传参来控制宽度
print('[%%-%ds]' %50) #[%-50s]
print(('[%%-%ds]' %50) %'#')
print(('[%%-%ds]' %50) %'##')
print(('[%%-%ds]' %50) %'###')


#=========实现打印进度条函数==========
import sys
import time

def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


#=========应用==========
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(0.5) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024

    percent=recv_size/data_size #接收的比例
    progress(percent,width=70) #进度条的宽度70