#!/usr/bin/env python
"""
import serial
import json
import time
import datetime
from time import sleep
import argparse
import sys
import os

now = datetime.datetime.now()
now
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)




ext_first= False

try:
	
	ser = serial.Serial('\\.\COM9', 115200,timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
	Ver_Mes="Version\r"
	Date_Mes="Date\r"
	Help_Mes="Help\r"
	Time_Mes="Time\r"
	List_MES=[Ver_Mes,Help_Mes]
	received_data =""

	for Message in List_MES:
		
		ser.write(Message.encode())
		time.sleep(1)
		#result=""
		while True:
			result = ser.readline().decode().strip()
			
			if "ext." in result:
				#if not ext_first:
				#	time.sleep(1)
				#	ext_first =True
				received_data += result[:result.index("ext.")] + "\n"
				result=""
				break
			
			received_data += result +"\n"
	received_data += "\n"+ "Time \n" + str(now.time()) +"\n"+  "Date \n"+str(now.date())+"\n"
	
	
	with open("the_note7.txt", 'w') as file:
			# Write content to the file
		file.write("testing")
			

			#file=open("the_note7.txt", "w")
			#file.write(str(received_data))
	


	
	
	
finally:
	print(received_data)
	#current_Date=datetime.date.today()		
	#print (current_Date)
	#current_Time=datetime.datetime.now().time()
	#print(current_Time)
	file.close()
	ser.close()
"""


#gpt
import os
import serial
import datetime
import time
now = datetime.datetime.now()
ext_first = False
received_data = ""
#file_path= ""
file = open("C:/Users/iurena/Downloads/Final_note4.txt", 'w')

#print("current working directory:", os.getcwd())
try:
   ser = serial.Serial('\\\\.\\COM9', 115200, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
   Ver_Mes = "Version\r"
   Date_Mes = "Date\r"
   Help_Mes = "Help\r"
   Time_Mes = "Time\r"
   List_MES = [Help_Mes,Ver_Mes ]
   for Message in List_MES:
       ser.write(Message.encode())
       time.sleep(1)
       while True:
           result = ser.readline().decode().strip()
           if "ext." in result:
               received_data += (result[:result.index("ext.")] + "\n" )
               break
           received_data += result + "\n"
   received_data += "\n"+ "Time \n" + "		"+ str(now.time()) + "\n" + "\n" + "Date \n"+"		" + str(now.date()) + "\n"
   #print(str(received_data))

   file.write(str(received_data))
   #print ('file created')
    


except FileNotFoundError:
    print("error: file not found")
except PermissionError:
	print("error: permission denined")



except Exception as e:
    print("Error:", e)
finally:
   print("process completed")
   file.close()
   ser.close()
   








