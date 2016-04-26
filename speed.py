import time
import paho.mqtt.client as paho
import datetime

client = paho.Client()
time.sleep(2)

RPIhostname = "node-R2"
RPIip = "192.168.0.103"

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("localhost", 1883, 60)

time_stamp = int(time.time()*1000000000)

arq = open('/home/azhang/jarova/python/speed-service/speedtest.txt', 'r')
textoPing = arq.readline()
textoDownload = arq.readline()
textoUpload = arq.readline()
arq.close()

testPingList = textoPing.split(" ")
testDownloadList = textoDownload.split(" ")
testUploadList = textoUpload.split(" ")

device = "Raspberry"
dataType = "METRIC"

#msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"Raspberry.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Latency",device,RPIhostname,RPIip,dataType,"Ping",testPingList[2],time_stamp,testPingList[1])

msg ='%s,Raspberry.id=%s,rpi.hostname=%s,rpi.ip=%s,rpi.datatype=%s,sensor.unit=%s,sensor.name=%s value=%s %s' % ("Latency",device,RPIhostname,RPIip,dataType,"ms","Ping",testPingList[1],time_stamp)
print msg
client.publish("javier/board1", msg)
time.sleep(0.1)

#msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"Raspberry.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("DownloadSpeed",device,RPIhostname,RPIip,dataType,"DownloadSpeed",testDownloadList[2],time_stamp,testDownloadList[1])

msg ='%s,Raspberry.id=%s,rpi.hostname=%s,rpi.ip=%s,rpi.datatype=%s,sensor.unit=%s,sensor.name=%s value=%s %s' % ("DownloadSpeed",device,RPIhostname,RPIip,dataType,"Mbit/s","DownloadSpeed",testDownloadList[1],time_stamp)
print msg
client.publish("javier/board1", msg)
time.sleep(0.1)

#msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"Raspberry.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("UploadSpeed",device,RPIhostname,RPIip,dataType,"UploadSpeed",testUploadList[2],time_stamp,testUploadList[1])

msg ='%s,Raspberry.id=%s,rpi.hostname=%s,rpi.ip=%s,rpi.datatype=%s,sensor.unit=%s,sensor.name=%s value=%s %s' % ("UploadSpeed",device,RPIhostname,RPIip,dataType,"Mbit/s","UploadSpeed",testUploadList[1],time_stamp)
print msg
client.publish("javier/board1", msg)
time.sleep(0.1)
