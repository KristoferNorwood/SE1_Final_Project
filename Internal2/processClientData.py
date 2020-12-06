#!/usr/bin/python

import socket
import intelligentModel
import clientThread
from lxml import etree as et
from typing import List
import logging

# def __init__(self, data, inStream):
# 	super().__init__()
# 	self.data = data
# 	self.inStream: socket = inStream
# 	self.diagnosis
# 	self.intelligentModel : intelligentModel
# 	self.myRoot
# 	self.verdict
# 	self.root
# 	self.sendDiagReq()
# 	self.diagnose()

def clientDiag(data):
	myLogger = logging.getLogger('myLogger')
	friendServers = [["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], 
		["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], 
		["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123]]
	root = et.fromstring(data) 
	i = 0
	j = 0
	diagnosis = []
	myRoot = et.tostring(root)
	# diagnosis.insert(3, 29)
	for i in range(12):
		s = socket.socket()
		s.settimeout(30)
		s.connect((friendServers[i][j],friendServers[i][j+1]))
		while True:
			s.send(bytes(myRoot))
			incomingVote = s.recv(65536)
			friendData = incomingVote.decode("utf8")
			diagnosis.insert(i, getFriendDiagnosis(friendData))
			s.close()
			break
	myDiag = intelligentModel(data)
	if(myDiag == 4):
		myLogger.info('Intelligent model diagnosis for Client is cancer')
	else:
		myLogger.info('Intelligent model diagnosis for Client is cancer')
	diagnosis.insert(12, myDiag)
	verdict = getVerdict(diagnosis)
	if(verdict):
		myLogger.info('result of intelligent model is cancer')
	else:
		myLogger.info('result of the intelligent model is not cancer')
	return verdict
	# verdict = getVerdict(diagnosis)
	# if verdict:
	# 	myDiag = 2
	# else:
	# 	myDiag = 4
	# for patient in root:
	# 	patient.find('class').text = str(myDiag)

def getVerdict(diagnosis):
	vote = 0
	vote1 = 0
	for num in diagnosis:
		if num == 2:
			vote += 1
		else:
			vote1 += 1
	if vote1 > vote:
		return True
	else:
		return False


def getFriendDiagnosis(data):
	diagnosis = ""
	root = et.fromstring(data) 
	for patient in root:
		diagnosis = patient.find('class').text
	diag = int(diagnosis)
	return diag