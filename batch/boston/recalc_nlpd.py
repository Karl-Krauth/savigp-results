import pandas as pd
import glob
import os
import numpy as np

folders = glob.glob('boston_*')
for folder in folders:
    data = pd.read_csv(os.path.join(folder, "predictions.csv"))
    preds = data.values
    test_y = preds[:,0]
    pred_mu = preds[:,1]
    pred_var = preds[:,2]
    print folder,test_y.shape, pred_mu.shape, pred_var.shape
    nlpd = (0.5 * (pred_mu - test_y) ** 2 / (pred_var) + 0.5 * np.log(2 * np.pi * pred_var))
    data['NLPD_0'] = nlpd
    data.to_csv(os.path.join(folder, "predictions.csv"), index=False)
