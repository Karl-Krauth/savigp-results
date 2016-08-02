from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np

gp_nlpd = np.empty([5, 1266])
gp_sse = np.empty([5, 1266])
warp_nlpd = np.empty([5, 1266])
warp_sse = np.empty([5, 1266])

for i in xrange(1, 6):
    data = loadmat("gp-creep-" + str(i) + ".mat")
    print data["sse"][:, 0].shape
    gp_sse[i - 1] = data["sse"][:, 0]
    gp_nlpd[i - 1] = data["nlpd"][:, 0]
    data = loadmat("warp-creep-" + str(i) + ".mat")
    warp_sse[i - 1] = data["sse"][:, 0]
    warp_nlpd[i - 1] = data["nlpd"][:, 0]

gp_nlpd = gp_nlpd.flatten()
gp_sse = gp_sse.flatten()
warp_nlpd = warp_nlpd.flatten()
warp_sse = warp_sse.flatten()

sse_file = sys.argv[1]
nlpd_file = sys.argv[2]

sse_data = pd.read_csv(sse_file)
print sse_data.shape
print gp_sse.shape
sse_data['GAUS:'] = gp_sse
sse_data['WARP:'] = warp_sse
sse_data.to_csv(sse_file, index=False)

nlpd_data = pd.read_csv(nlpd_file)
nlpd_data['GAUS:'] = gp_nlpd
nlpd_data['WARP:'] = warp_nlpd
nlpd_data.to_csv(nlpd_file, index=False)

