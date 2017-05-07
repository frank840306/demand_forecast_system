# import requests
import csv
import pickle
# from pyquery import PyQuery as pq
from random import randint
import os

# def readCSV(fin):
# 	with open(fin, 'r') as file:
# 		content = list(csv.reader(file, delimiter=',', quotechar='|'))
# 	return content[0], content[1:]
def randAuthor(author_num):
	lists = [0] * author_num
	for i in range(author_num):
		lists[i] = randint(1, 100)
	return lists

def defineAuthor(author_num):
	lists = [0] * author_num
	for i in range(author_num):
		if i == 0 or i == 1 or i == 10 or i == 11 or i == 12:
			lists[i] = 0	
		elif i == 2 or i == 3 or i == 4 or i == 13 or i == 14:
			lists[i] = 1
		elif i == 5 or i == 15 or i == 16 or i == 17 or i == 18:
			lists[i] = 2
		elif i == 7 or i == 8 or i == 9 or i == 19:
			lists[i] = 3
		else:			
			lists[i] = i // 5
	return lists

def getAuthor(productList):
	# field_name, productList = readCSV(PRODUCT_CSV)
	# authorID = randAuthor(len(productList))
	authorID = defineAuthor(len(productList))
	for idx in range(len(productList)):
		book_name = productList[idx][2]
		productList[idx].append(authorID[idx])
		# print(productList[idx])
	return productList

def getProductToAuthorMap(productList):
	dicts = {}
	for i in range(len(productList)):
		# print(productList[i][0] + ' ' + str(productList[i][5]))
		dicts[int(productList[i][0])] = productList[i][5]
	return dicts

def getProductToTypeMap(productList):
	dicts = {}
	for i in range(len(productList)):
		dicts[int(productList[i][0])] = productList[i][1]
	return dicts

def getProductMap(productList):
	dicts = {}
	for i in range(len(productList)):
		dicts[int(productList[i][0])] = productList[i][2]
	return dicts

def getCustomerMap(consumerList):
	dicts = {}
	for i in range(len(consumerList)):
		dicts[int(consumerList[i][0])] = consumerList[i][1]
	return dicts
