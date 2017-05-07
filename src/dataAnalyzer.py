from utils import *
import numpy as np
import myMF

root_dir = './' 
data_dir = os.path.join(root_dir, 'data')
output_dir = os.path.join(root_dir, 'output')

PRODUCT2AUTHOR_PKL = os.path.join(data_dir, "Frank_product2author.pkl")
PRODUCT2TYPE_PKL = os.path.join(data_dir, "Frank_product2type.pkl")

IDX2CONSUMER_PKL = os.path.join(data_dir, 'Frank_idx2consumer.pkl')
IDX2PRODUCT_PKL = os.path.join(data_dir, 'Frank_idx2product.pkl')

PRODUCT_CONSUMER_MATRIX_PKL = os.path.join(data_dir, 'Frank_product_consumer_matrix.pkl')	# 2d numpy sparse matrix
AUTHOR_CONSUMER_MATRIX_PKL = os.path.join(data_dir, 'Frank_author_consumer_matrix.pkl')

AUTHOR2CLUSTERIDX_PKL = os.path.join(data_dir, 'Frank_author2clusterIdx.pkl')

def getAuthorProportion(mat, product2author):
	author_dicts = {}
	total_sum = 0
	
	for product_idx in range(len(mat)):
		if (product_idx + 1) not in product2author:
			print('key error : product idx = ' + product_idx + 1)
		else:
			if product2author[product_idx + 1] not in author_dicts:
				author_dicts[ product2author[product_idx + 1] ] = mat[product_idx]
			else:
				author_dicts[ product2author[product_idx + 1] ] += mat[product_idx]
			total_sum += mat[product_idx]
	
	for key in author_dicts:
		author_dicts[key] /= total_sum
	original_dicts = author_dicts.copy()
	author_dicts['other'] = 0
	
	keys = [k for k, v in author_dicts.items() if author_dicts[k] < 0.01]
	for key in keys:
		# author_dicts[key] /= total_sum
		if key != 'other':
			author_dicts['other'] += author_dicts[key]
			del author_dicts[key]
	print (author_dicts['other'])
	return original_dicts, author_dicts

def getTypeProportion(mat, product2type):
	type_dicts = {}
	total_sum = 0
	for product_idx in range(len(mat)):
		if (product_idx + 1) not in product2type:
			print('key error : product idx = ' + str(product_idx + 1))
		else:
			if product2type[product_idx + 1] not in type_dicts:
				type_dicts[ product2type[product_idx + 1] ] = mat[product_idx]
			else:
				type_dicts[ product2type[product_idx + 1] ] += mat[product_idx]
			total_sum += mat[product_idx]
	
	for key in type_dicts:
		type_dicts[key] /= total_sum
	original_dicts = type_dicts.copy()
	type_dicts['other'] = 0

	keys = [k for k, v in type_dicts.items() if type_dicts[k] < 0.01]

	for key in keys:
		if key != 'other':
			type_dicts['other'] += type_dicts[key]
			del type_dicts[key]
			
	return original_dicts, type_dicts	

def getClusterProportion(autConMat, autCluster):
	# for i in autConMat:
	# 	print (i)
	# print(autConMat.shape)
	# return
	clusterProportion = np.zeros(len(autCluster))
	for cluster_idx in range(len(autCluster)):
		tmp = np.zeros(300)
		for author_idx in autCluster[cluster_idx]:
			tmp = np.logical_or(tmp, autConMat[author_idx])

		clusterProportion[cluster_idx] = np.sum(tmp)
	clusterSum = np.sum(clusterProportion)
	clusterProportion /= clusterSum
	# for cluster in clusterProportion:
	# 	cluster = cluster / clusterSum
	# 	print(cluster)
	# print(clusterSum)
	# print(clusterProportion)
	
	return clusterProportion

def outputAnalysisResult(info):
	for key in info:
		fout = os.path.join(output_dir, key + '.pkl')
		writePickle(fout, info[key])
	writePickle(os.path.join(output_dir, 'info.pkl'), info)
def dataAnalyzer():
	info = {}
	#  cluster the author
	proConMat = readPickle(PRODUCT_CONSUMER_MATRIX_PKL)
	autConMat = readPickle(AUTHOR_CONSUMER_MATRIX_PKL)
	product2type = readPickle(PRODUCT2TYPE_PKL)
	product2author = readPickle(PRODUCT2AUTHOR_PKL)
	# for i in autConMat:
	# 	print (i)
	# print(np.sum(np.sum(autConMat)))
	# print (np.sum(autConMat[:300, :], axis=0))
	############# MF #############
	LOAD_MODEL = True if os.path.exists(AUTHOR2CLUSTERIDX_PKL) else False
	
	if LOAD_MODEL:
		print('loading MF model')	
		author_label = readPickle(AUTHOR2CLUSTERIDX_PKL)
	else:
		print('training MF model')		
		accountMat = autConMat[:, :300]
		cluster_num = 30 # 80
		latent_num = 40
		author_label = myMF.fit(accountMat, cluster_num, latent_num)
		writePickle(AUTHOR2CLUSTERIDX_PKL, author_label)

	author_cluster = {}
	# author2clusterIdx = {}
	for author_idx in range(len(author_label)):
		if author_label[author_idx] not in author_cluster:
			author_cluster[ author_label[author_idx] ] = [author_idx]
		else:
			author_cluster[ author_label[author_idx] ].append(author_idx)
	
	clusterProportion = getClusterProportion(autConMat[:, :300], author_cluster)
	print(clusterProportion)
	info['author2clusterIdx'] = author_label
	info['clusterOfAuthor'] = author_cluster
	info['clusterProportion'] = clusterProportion

	###### history consuming #####
	SumProductMat = np.sum(proConMat, axis=1)
	
	info['totalConsuming'] = np.sum(SumProductMat)
	info['oriTypeProportion'], info['typeProportion'] = getTypeProportion(SumProductMat, product2type)
	info['oriAuthorProportion'], info['authorProportion'] = getAuthorProportion(SumProductMat, product2author)
	# print(info['oriTypeProportion'])
	##############################
	
	outputAnalysisResult(info)
	
if __name__ == '__main__':
	dataAnalyzer()