# ��ɫ���� 
# ѡ����
#V2.0
#���б���ļ�����Ϊ�ַ������ӳ���������ԣ�
#V3.0
#�޸���ʾ����������ƥ�������
#V3.1
#�޸���ʾ����������ƥ������� ��ʱ���ǩ
#V3.2
#�޸���ʾ���������౶ģʽ 
#v7.0
#�޸��жϷ�ʽ�����ٶ�
#v7.0b
#�޸�Ϊ�������һ���ж�
#v8.0
#�����ʼ����ͽ���ķ��� �������óɶ��Ž��� ����ɹ�  ��һ�� ���������Զ��ɼ���� �Ͷ��߳�֧�� ������δ��
#v8.01
#�������Ϊ�ƶ����ļ�
#-*-coding:utf-8-*-  
import random
import time
import smtplib,re
from email.mime.text import MIMEText
def send (fromail,passwd,tomail,sub,info):#�ʼ����ͺ���
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
com_number=["17","22","26","27","33",["06","10"]]#���������
fp = open("ob.txt","w")
fp1 = open("dlt.txt","a")#�޸Ĵ�
out=[]
def maicai():
    #�������ݳ�
    c=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
    d=[]
    my=[]
    my1=[]
    for i in range(0,5,1):
         YY=random.choice(c)
         d.append(YY)
         c.remove(YY)
    my=d
    #print(my) #��ʾԭʼ������my
    global my_number
	
    #my.sort()#��ʽ������
	
	
    a=["01","02","03","04","05","06","07","08","09","10","11","12"]
    b=[]
	
    for p in range(0,2,1):
	    YY=random.choice(a);b.append(YY);a.remove(YY)
    my1=b
    my1.sort()
    my.append(my1)
	
    my_number.append(my)
    #print(my)#��ʾ����������my
        
    #������������鵽my_number
    #a=time.strftime("[%Y %m %d %H:%M:%S] ",time.localtime())#��ʱ���ǩ
    #a=time.strftime("[%H:%M:%S]",time.localtime())#ʱ���ǩ
    #my_number.append(a)
    #print(a)#��ʾʱ���ǩ����
    #time.sleep(3)#�ȴ�����
    #print(my_number)#��ʾ����my_number

def duijiang(i):
    global com_number
    global my_number
    #�����ַ���
    #txt=str(i)+".txt"
    
    
    com_number=str(com_number)
    my_number1=str(my_number)
    #if my_number.find(com_number):
    
    a=my_number1.count(com_number)

    print("com_number������my_number�г���"+str(a)+"�Σ�")
    #ͳ��com_number�������г��ָ���
    for i in range(0,a,1):


        number=[]
        b=my_number1.find(com_number)
        number=my_number1[b:]
        number=str(number)
        #print(b)#��ʾ�ֶ�com_number��my_number�е�λ�á�
        c=number[0:132]+"\n"#��ʾ��һ�������ǰһ�����#�޸Ĵ�
        #print(c,file=fp1)#�޸Ĵ�
	fp1.write(c)#�޸Ĵ�
        print(c)
        #send('w-f108@163.com','wppplwang','13659398903@139.com','Use My Python',c) #�ʼ����ͽ������

        out.append(c)
        #print(out)
        my_number1=number[105:]#�ڴ˶��ȡ���ļ�һ��, ��������� �ļ����һ�����޸����ٿ�����
        
        
        
        
        
        #time.sleep(1)
# main in this Program Files ��������

for i in range (0,50000,1):
    my_number=[]#���һ��û��my_number
    out=[]#���һ��û��out
    print (i)
    for m in range (0,1111111,1):#�������������ѭ������
        maicai()

    duijiang(i)
    fp.write(str(out))
    #fp1.write(str(sort(out)))
    
print("��Ϸ����!")
fp.close() 
fp1.close()#�޸Ĵ�
send('w-f108@163.com','wppplwang','13659398903@139.com','Use My Python','........') #�ʼ����ͽ������