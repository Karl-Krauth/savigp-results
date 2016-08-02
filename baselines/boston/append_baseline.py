from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np

nlpd = np.empty([5, 206])
sse = np.empty([5, 206])

for i in xrange(1, 6):
    data = loadmat("gp-boston-" + str(i) + ".mat")
    sse[i - 1] = data["sse"][:, 0]
    nlpd[i - 1] = data["nlpd"][:, 0]

nlpd = nlpd.flatten()
sse = sse.flatten()

sse_file = sys.argv[1]
nlpd_file = sys.argv[2]

sse_data = pd.read_csv(sse_file)
sse_data['BASE:'] = sse
sse_data.to_csv(sse_file, index=False)

nlpd_data = pd.read_csv(nlpd_file)
nlpd_data['BASE:'] = nlpd
nlpd_data.to_csv(nlpd_file, index=False)

