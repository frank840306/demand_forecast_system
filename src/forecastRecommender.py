from utils import *
from samplePublisherData import sampleData
import numpy as np
import os

root_dir = './'
output_dir = os.path.join(root_dir, 'output')
INFO_PKL = os.path.join(output_dir, 'info.pkl')


A = 0.3
B = 0.5

def getRatioOfBook(book_attr):
	book_ratio = {}
	clusterSum = 0
	authorSum = 0
	typeSum = 0
	for book in book_attr:
		clusterSum += book_attr[book]['clusterAttr']
		authorSum += book_attr[book]['authorAttr']
		typeSum += book_attr[book]['typeAttr']
	for book in book_attr:
		tmp1 = book_attr[book]['clusterAttr'] / clusterSum
		tmp2 = book_attr[book]['authorAttr'] / authorSum
		tmp3 = book_attr[book]['typeAttr'] / typeSum
		book_ratio[book] = (tmp1 * A + tmp2 * (1 - A)) * B + tmp3 * (1 - B)
	
	print(book_ratio)
	return book_ratio

def predict():
	info = readPickle(INFO_PKL)

	publisherData = sampleData()
	publisherBudge = {
		'publisher_A' : 0.5,
		'publisher_B' : 0.3,
		'publisher_C' : 0.2
	}

	# publisherBudge = np.array([0.5, 0.3, 0.2]) * info['totalConsuming'] * 10 # us dollar
	# print(publisherBudge)
	publisherRatio = {}
	for publisher in publisherData :
		book_attr = {}
		for book in publisherData[publisher]:
			# print(info['author2clusterIdx'])
			# print(info['clusterOfAuthor'])
			book_attr[book] = {}
			book_attr[book]['clusterAttr'] = info['clusterProportion'] [ info['author2clusterIdx'] [ publisherData[publisher][book]['author'] ] ]
			book_attr[book]['authorAttr'] = info['oriAuthorProportion'][publisherData[publisher][book]['author']]
			book_attr[book]['typeAttr'] = info['oriTypeProportion'][publisherData[publisher][book]['type']]
			# book_attr.append([tmp1, tmp2, tmp3])
		# print(book_attr)
		book_ratio = getRatioOfBook(book_attr)
		publisherRatio[publisher] = book_ratio 
	for publisher in publisherRatio:
		for book in publisherRatio[publisher]:
			publisherRatio[publisher][book] *= publisherBudge[publisher] * info['totalConsuming']
		# publisherRatio[publisher] *= publisherBudge[publisher] * 10 * info['totalConsuming']
	
	return publisherRatio

if __name__=='__main__':
	predict()