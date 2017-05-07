import getAuthor
import getConsumerProductMatrix
import myMF
from utils import *

root_dir = './' 
data_dir = os.path.join(root_dir, 'data')
PRODUCT_CSV = os.path.join(data_dir, 'PRODUCT_MST.csv')
CONSUMER_CSV = os.path.join(data_dir, 'CUSTOMER_MST.csv')

PRODUCT_AUTHOR_PKL = os.path.join(data_dir, 'Frank_product_author.pkl')			# 2d list

PRODUCT2AUTHOR_PKL = os.path.join(data_dir, "Frank_product2author.pkl")
PRODUCT2TYPE_PKL = os.path.join(data_dir, "Frank_product2type.pkl")
IDX2CONSUMER_PKL = os.path.join(data_dir, 'Frank_idx2consumer.pkl')
# IDX2AUTHOR_PKL = os.path.join(data_dir, 'Frank_idx2author.pkl')
IDX2PRODUCT_PKL = os.path.join(data_dir, 'Frank_idx2product.pkl')

PRODUCT_CONSUMER_MATRIX_PKL = os.path.join(data_dir, 'Frank_product_consumer_matrix.pkl')	# 2d numpy sparse matrix
AUTHOR_CONSUMER_MATRIX_PKL = os.path.join(data_dir, 'Frank_author_consumer_matrix.pkl')
def createData():
	# if not os.path.exists(PRODUCT2TYPE_PKL):
	productList = readCSV(PRODUCT_CSV)[1:]
	consumerList = readCSV(CONSUMER_CSV)[1:]
	productList = getAuthor.getAuthor(productList)[:500]
	idxProduct2Author = getAuthor.getProductToAuthorMap(productList)
	idxProduct2Type = getAuthor.getProductToTypeMap(productList)

	idx2product = getAuthor.getProductMap(productList)
	idx2consumer = getAuthor.getCustomerMap(consumerList)
	
	writePickle(IDX2CONSUMER_PKL, idx2consumer)
	writePickle(IDX2PRODUCT_PKL, idx2product)
	writePickle(PRODUCT2AUTHOR_PKL, idxProduct2Author)
	writePickle(PRODUCT2TYPE_PKL, idxProduct2Type)
	writePickle(PRODUCT_AUTHOR_PKL, productList)

	# if not os.path.exists(AUTHOR_CONSUMER_MATRIX_PKL):
	print('create author consumer matrix pkl')
	consumerList = readCSV(CONSUMER_CSV)[1:]
	productList = readPickle(PRODUCT_AUTHOR_PKL)
	proConMat = getConsumerProductMatrix.getProConMatrix()
	autConMat = getConsumerProductMatrix.getAutConMatrix(proConMat)
	writePickle(PRODUCT_CONSUMER_MATRIX_PKL, proConMat)
	writePickle(AUTHOR_CONSUMER_MATRIX_PKL, autConMat)
	
	autConMat = readPickle(AUTHOR_CONSUMER_MATRIX_PKL)
	# data for MF
	accountMat = autConMat[:, :300]
	#data for other analysis
	noAccMat = autConMat[:, 300:]
	

	######### MF #########
	# myMF.MF(accountMat)




	# print(accountMat.shape)
	# print(noAccMat.shape)

if __name__=='__main__':
	createData()