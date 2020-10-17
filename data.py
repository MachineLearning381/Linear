from numpy import random
from sklearn import datasets


iris_X = datasets.load_iris().data
iris_Y = datasets.load_iris().target
# 150 total samples
#s1   10%   15 samples
#s2   20%   30 samples
#s3   30%   45 samples
#s4   40%   60 samples
#s5   50%   75 samples

s1_I = np.random.choice(iris.shape[0], 15, replace=False)
s2_I = np.random.choice(iris.shape[0], 30, replace=False)
s3_I = np.random.choice(iris.shape[0], 45, replace=False)
s4_I = np.random.choice(iris.shape[0], 60, replace=False)
s5_I = np.random.choice(iris.shape[0], 75, replace=False)

iris_s1_X = iris_X[s1_I]
iris_s2_X = iris_X[s2_I]
iris_s3_X = iris_X[s3_I]
iris_s4_X = iris_X[s4_I]
iris_s5_X = iris_X[s5_I]

iris_s1_Y = iris_Y[s1_I]
iris_s2_Y = iris_Y[s2_I]
iris_s3_Y = iris_Y[s3_I]
iris_s4_Y = iris_Y[s4_I]
iris_s5_Y = iris_Y[s5_I]





breast_cancer_X = datasets.load_breast_cancer().data
breast_cancer_Y = datasets.load_breast_cancer().target
#569 total samples
#s1   10%   57 samples
#s2   20%   114 samples
#s3   30%   171 samples
#s4   40%   228 samples
#s5   50%   285 samples

s1_B = np.random.choice(breastCancer.shape[0], 57, replace=False)
s2_B = np.random.choice(breastCancer.shape[0], 114, replace=False)
s3_B = np.random.choice(breastCancer.shape[0], 171, replace=False)
s4_B = np.random.choice(breastCancer.shape[0], 228, replace=False)
s5_B = np.random.choice(breastCancer.shape[0], 285, replace=False)

breastCancer_s1_X = breastCancer_X[s1_B]
breastCancer_s2_X = breastCancer_X[s2_B]
breastCancer_s3_X = breastCancer_X[s3_B]
breastCancer_s4_X = breastCancer_X[s4_B]
breastCancer_s5_X = breastCancer_X[s5_B]

breastCancer_s1_Y = breastCancer_Y[s1_B]
breastCancer_s2_Y = breastCancer_Y[s2_B]
breastCancer_s3_Y = breastCancer_Y[s3_B]
breastCancer_s4_Y = breastCancer_Y[s4_B]
breastCancer_s5_Y = breastCancer_Y[s5_B]
