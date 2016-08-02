from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np

ep_nlpd = np.empty([5, 1232])
ep_er = np.empty([5, 1])

for i in xrange(1, 6):
    data = loadmat("emtboh-usps-" + str(i) + ".mat")
    ep_er[i - 1] = data["errorrate"][:, 0]
    ep_nlpd[i - 1] = data["nlpd"][:, 0]

ep_nlpd = ep_nlpd.flatten()
ep_er = ep_er.flatten()

er_file = sys.argv[1]
nlpd_file = sys.argv[2]

er_data = pd.read_csv(er_file)
print er_data.shape
print ep_er.shape
er_data['EMTB:'] = ep_er
er_data.to_csv(er_file, index=False)

nlpd_data = pd.read_csv(nlpd_file)
nlpd_data['EMTB:'] = ep_nlpd
nlpd_data.to_csv(nlpd_file, index=False)

