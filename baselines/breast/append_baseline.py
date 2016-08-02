from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np

ep_nlpd = np.empty([5, 383])
ep_er = np.empty([5, 1])
vb_nlpd = np.empty([5, 383])
vb_er = np.empty([5, 1])

for i in xrange(1, 6):
    data = loadmat("ep-breast-" + str(i) + ".mat")
    ep_er[i - 1] = data["errorRate"][:, 0]
    ep_nlpd[i - 1] = data["nlpd"][:, 0]
    data = loadmat("vb-breast-" + str(i) + ".mat")
    vb_er[i - 1] = data["errorRate"][:, 0]
    vb_nlpd[i - 1] = data["nlpd"][:, 0]

ep_nlpd = ep_nlpd.flatten()
ep_er = ep_er.flatten()
vb_nlpd = vb_nlpd.flatten()
vb_er = vb_er.flatten()

er_file = sys.argv[1]
nlpd_file = sys.argv[2]

er_data = pd.read_csv(er_file)
print er_data.shape
print ep_er.shape
er_data['EXPP:'] = ep_er
er_data['VARB:'] = vb_er
er_data.to_csv(er_file, index=False)

nlpd_data = pd.read_csv(nlpd_file)
nlpd_data['EXPP:'] = ep_nlpd
nlpd_data['VARB:'] = vb_nlpd
nlpd_data.to_csv(nlpd_file, index=False)

