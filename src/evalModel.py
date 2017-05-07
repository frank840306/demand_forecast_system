import numpy as np
from sklearn.cluster import KMeans
from utils import *
import os

root_dir = './'
data_dir = os.path.join(root_dir, 'data')
model_dir = os.path.join(root_dir, 'MF_model')

finModel = os.path.join(model_dir, 'MF_model_author_5000_err_46.pkl')

MFmodel = readPickle(finModel)

print(MFmodel.shape)

kmeans = KMeans(n_clusters=80, random_state=0).fit(MFmodel)
print(kmeans.labels_)
