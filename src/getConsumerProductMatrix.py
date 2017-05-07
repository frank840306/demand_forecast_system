import numpy as np
from random import randint

product_type_num = 500
best_seller_type_num = 10
author_num = 100

consuming_num = 6000
account_num = 300


def getUniform(idx, len, total_len):
	idx = int(idx)
	a = [0] * total_len
	for i in range(len):
		a[i + idx] = (randint(-5, 5) / 100) + 1
	normal_size = sum(a)
	for i in range(len):
		a[i + idx] /= normal_size
	return np.array(a)


def testCol():
	return True
def testRow():
	return True
def getDisForProduct(types):
	if types == 1:
		disArrT = np.zeros((best_seller_type_num, account_num))
		disArrT[0] = getUniform(0, 160, 300)
		disArrT[1] = getUniform(0, 160, 300)
		disArrT[2] = getUniform(2, 160, 300)
		disArrT[3] = getUniform(3, 160, 300)
		disArrT[4] = getUniform(1, 160, 300)
		disArrT[5] = getUniform(130, 160, 300)
		disArrT[6] = getUniform(131, 160, 300)
		disArrT[7] = getUniform(133, 160, 300)
		disArrT[8] = getUniform(130, 160, 300)
		disArrT[9] = getUniform(132, 160, 300)
		return disArrT
	elif types == 2:
		disArrT = np.zeros((product_type_num - best_seller_type_num, account_num))
		for i in range(product_type_num - best_seller_type_num):
			disArrT[i] = getUniform(10 * (i / 100), 200, 300)
		return disArrT
	elif types == 3:
		disArrT = np.zeros((best_seller_type_num, consuming_num - account_num))
		disArrT[0] = getUniform(0, 910, 5700)
		disArrT[1] = getUniform(31, 910, 5700)
		disArrT[2] = getUniform(26, 910, 5700)
		disArrT[3] = getUniform(38, 910, 5700)
		disArrT[4] = getUniform(32, 910, 5700)
		disArrT[5] = getUniform(1000, 910, 5700)
		disArrT[6] = getUniform(1110, 910, 5700)
		disArrT[7] = getUniform(1330, 910, 5700)
		disArrT[8] = getUniform(880, 910, 5700)
		disArrT[9] = getUniform(770, 910, 5700)
		return disArrT

	elif types == 4:
		disArrT = np.zeros((product_type_num - best_seller_type_num, consuming_num - account_num))
		for i in range(product_type_num - best_seller_type_num):
			disArrT[i] = getUniform(10 * (i / 100), 2000, 5700)
		return disArrT
	else:
		return []
# sss = 0
	
def randForAccount(matRow, disRow, rank):
	# print(sorted(disRow)[:20])
	thres = sorted(disRow, reverse=True)[rank]
	# print(thres)
	for idx in range(len(disRow)):
		# matRow[idx] = 1 if disRow[idx] > thres else 0
		if disRow[idx] > thres:
			# print(matRow[idx])
			matRow[idx] = 1
		else:
			matRow[idx] = 0
	return

def getProConMatrix():
	productDis1 = getDisForProduct(1)
	productDis2 = getDisForProduct(2)
	productDis3 = getDisForProduct(3)
	productDis4 = getDisForProduct(4)
	tmpAcc = np.concatenate((productDis1, productDis2), axis=0)
	noAcc = np.concatenate((productDis3, productDis4), axis=0)
	disMat = np.concatenate((tmpAcc, noAcc), axis=1)
	# for i in disMat[450]:	
	# 	print(i)
	for product_idx in range(product_type_num):
		disMat[product_idx] /= sum(disMat[product_idx])
	mat = np.zeros((product_type_num, consuming_num))
	for product_type_idx in range(product_type_num):
		if product_type_idx < best_seller_type_num:
			randForAccount(mat[product_type_idx], disMat[product_type_idx], 1070)
		else:
			randForAccount(mat[product_type_idx], disMat[product_type_idx], 15)
	# smoothing
	sumConsuming = np.sum(mat, axis=0)
	for consuming_idx in range(consuming_num):
		if sumConsuming[consuming_idx] == 0:
			mat[randint(0, 499)][consuming_idx] = 1
	
	# print (np.sum(np.sum(mat)))
	return mat

def getAutConMatrix(conProMat):
	conAutMat = np.zeros((author_num, consuming_num))
	for product_idx in range(product_type_num):
		if product_idx == 0 or product_idx == 1 or product_idx == 10 or product_idx == 11 or product_idx == 12:
			conAutMat[0] += conProMat[product_idx]
		elif product_idx == 2 or product_idx == 3 or product_idx == 4 or product_idx == 13 or product_idx == 14:
			conAutMat[1] += conProMat[product_idx]
		elif product_idx == 5 or product_idx == 15 or product_idx == 16 or product_idx == 17 or product_idx == 18:
			conAutMat[2] += conProMat[product_idx]
		elif product_idx == 6 or product_idx == 7 or product_idx == 8 or product_idx == 9 or product_idx == 19:
			conAutMat[3] += conProMat[product_idx]
		else:
			conAutMat[product_idx // 5] += conProMat[product_idx]
	return conAutMat
	
if __name__== '__main__':
	mat = getMatrix([], [])