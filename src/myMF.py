import numpy as np
from sklearn.cluster import KMeans
from utils import *
import os

root_dir = './'
data_dir = os.path.join(root_dir, 'MF_model')
fout_base = os.path.join(data_dir, 'MF_model')

def matrix_factorization(R, author_attr, consumer_attr, K, steps=2500, alpha=0.005, beta=0.02):
    consumer_attr = consumer_attr.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(author_attr[i,:],consumer_attr[:,j])
                    for k in range(K):
                        author_attr[i][k] = author_attr[i][k] + alpha * (2 * eij * consumer_attr[k][j] - beta * author_attr[i][k])
                        consumer_attr[k][j] = consumer_attr[k][j] + alpha * (2 * eij * author_attr[i][k] - beta * consumer_attr[k][j])
        eR = np.dot(author_attr,consumer_attr)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - np.dot(author_attr[i,:],consumer_attr[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(author_attr[i][k],2) + pow(consumer_attr[k][j],2))
        print('step = ' + str(step) + ' , error = ' + str(e))
        if step % 100 == 99:
            print('===== write model ' + str(step + 1) + ' =====')

            foutR = fout_base + '_ori_' +  str(step + 1) + '_err_' + str(int(e)) + '.pkl'
            foutAuthor = fout_base + '_author_' + str(step + 1) + '_err_' + str(int(e)) + '.pkl'
            writePickle(foutR, R)
            writePickle(foutAuthor, author_attr)
        if e < 100:
            break
    
    return author_attr, consumer_attr.T

def fit(mat, cluster_num=80, latent_num=40):
    author_num, consumer_num = mat.shape
    # latent_num = 40

    author_attr = np.random.rand(author_num, latent_num)
    consumer_attr = np.random.rand(consumer_num, latent_num)

    new_author_attr, new_consumer_attr = matrix_factorization(mat, author_attr, consumer_attr, latent_num)
    # print(new_author_attr)
    
    kmeans = KMeans(n_clusters=cluster_num, random_state=0).fit(new_author_attr)
    print(kmeans.labels_)
    
    return kmeans.labels_
    # kmeans = KMeans(n_clusters=80, random_state=0).fit(mat)
    # print(kmeans.labels_)