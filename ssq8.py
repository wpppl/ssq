﻿
#V2.0
#改列表的文件类型为字符。增加程序的美观性！
#V3.0
#修改显示结果和输出不匹配的问�?
#V3.1
#修改显示结果和输出不匹配的问�?加时间标�?
#V3.2
#修改显示结果和输出多倍模�?
#v7.0
#修改判断方式提升速度
#v7.0b
#修改为红号蓝号一起判断
#v8.0
#增加邮件发送结果的方法 可以设置成短信接收 方便采购  下一步 打算升级自动采集结果 和多线程支持 其他的未定
#v8.01
#设置输出为制定的文件
#-*-coding:utf-8-*-  
import random
import time
import smtplib,re
from email.mime.text import MIMEText
def send (fromail,passwd,tomail,sub,info):#邮件发送函数
        msg = MIMEText(info)
        msg['Subject'] = sub
        msg['From'] = fromail
        smtp = smtplib.SMTP()
        p=re.compile(r'.*@(.*)')
        cn=p.findall(fromail)[0]
        smtp.connect(r'smtp.'+cn)
        smtp.login(fromail, passwd)
        smtp.sendmail(fromail,[tomail], msg.as_string())
        smtp.close()
		
		

my_number=[]
com_number=["17","01","09","33","07","20","08"]#这个不解�?
fp = open("ob.txt","w")
fp1 = open("ssq.txt","a")#修改�?
out=[]
def maicai():
    #创建数据�?
    c=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33"]
    d=[]
    my=[]
    for i in range(0,6,1):
         YY=random.choice(c)
         d.append(YY)
         c.remove(YY)
    my=d
    #print(my) #显示原始的数组my
    global my_number
	
    #my.sort()#格式化数�?
	
	
    a=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16"]
 
    YY=random.choice(a)
    my.append(YY)
   
	
    my_number.append(my)
    #print(my)#显示排序后的数组my
        
    #添加排序后的数组到my_number
    #a=time.strftime("[%Y %m %d %H:%M:%S] ",time.localtime())#长时间标�?
    #a=time.strftime("[%H:%M:%S]",time.localtime())#时间标签
    #my_number.append(a)
    #print(a)#显示时间标签开�?
    #time.sleep(3)#等待三秒
    #print(my_number)#显示数组my_number

def duijiang(i):
    global com_number
    global my_number
    #数组字符�?
    #txt=str(i)+".txt"
    
    
    com_number=str(com_number)
    my_number1=str(my_number)
    #if my_number.find(com_number):
    
    a=my_number1.count(com_number)

    #print("com_number在数组my_number中出�?+str(a)+"次！")
    #统计com_number在数组中出现个数
    for i in range(0,a,1):


        number=[]
        b=my_number1.find(com_number)
        number=my_number1[b:]
        number=str(number)
        #print(b)#显示字段com_number在my_number中的位置�?
        c=number[37:186]+"\n"#显示下一个结果和前一个结�?修改�?
        #print(c,file=fp1)#修改�?
        fp1.write(c)#修改�?
        print(c)
        #send('w-f108@163.com','wppplwang','13659398903@139.com','Use My Python',c) #邮件发送结果调用
        out.append(c)
        #print(out)
        my_number1=number[105:]#在此多截取了文件一�? 又在这错�?文件输出一样！修改了再看看�?
        
        
        
        
        
        #time.sleep(1)
# main in this Program Files （主程序�?

for i in range (0,10000000,1):
    my_number=[]#清空一次没有my_number
    out=[]#清空一次没有out
    print (i)
    for m in range (0,1111111,1):#在这里可以设置循环次�?
        maicai()

    duijiang(i)
    fp.write(str(out))
    #fp1.write(str(sort(out)))
    
print("游戏结束!")
fp.close() 
fp1.close()#修改�?
