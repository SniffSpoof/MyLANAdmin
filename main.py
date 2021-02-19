import socket
import time
import sys
import subprocess

#constants
menu = "-" * 50 + "Menu" + "-" * 50 + "\n(0)Settings\n(1)MyLAN\n(2)PortScanner\n(3)Ping\n(4)TraceRoute\n(5)RouterControl\n(99)Exit"
#/constants

class Tools():
	def __init__(self):
		pass

	def ping(self, domenOrIP, apts):
		command = ["ping", "domenOrIP", "-c", apts]
		proc = Popen(
    			command,
    			shell=True,
    			stdout=PIPE, stderr=PIPE
		)
		proc.wait()    # дождаться выполнения
		res = proc.communicate()  # получить tuple('stdout', 'stderr')
		if proc.returncode:
    			print res[1]
		print ('result:', res[0])

	def traceroute(self, domenOrIP):
		command = ["traceroute", "domenOrIP"]
		proc = Popen(
    			command,
    			shell=True,
    			stdout=PIPE, stderr=PIPE
		)
		proc.wait()    # дождаться выполнения
		res = proc.communicate()  # получить tuple('stdout', 'stderr')
		if proc.returncode:
    			print res[1]
		print ('result:', res[0])

	def PortScan(self):
		pass #TODO:Write me
	
	def TruePrintInShell(self, text):
		pass #TODO:Write me

class ClientPanel():
	#(0)settings
	#(1)MyLan
	#(2)PortScaner
	#(3)Ping
	#(4)Traceroute
	#(5)RouterControl
	#(99)Exit

	def __init__(self):
		pass
		#TODO:Write me

	def exit(self):
		print("Ave LocalHost\nAve sudo\nAve-Ave sys.Admin!")
		time.sleep(7)
