from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np
OFFSET = 191.0 / 811.0

def compute_vals(points):
    pre_mean = points.mean(axis=1)
    pre_var = points.var(axis=1)
    mean = np.exp(pre_mean + pre_var / 2) * OFFSET
    var = (np.exp(pre_var) - 1) * np.exp(2 * pre_mean + pre_var) * OFFSET ** 2
    # q2_5 = np.exp(pre_mean - np.sqrt(pre_var) * 1.96) * OFFSET
    # q97_5 = np.exp(pre_mean + np.sqrt(pre_var) * 1.96) * OFFSET
    return mean[:, np.newaxis], var[:, np.newaxis]# , q2_5, q97_5

ess_data = loadmat("ess-mining-39634972809487.mat")
x = ess_data['x']/365 + 1851.2026

ess_points = ess_data["posts"]["F"][0, 0]
hmc_points = loadmat("hmc-mining-36640043425887.mat")["posts"]["F"][0, 0]
ess_mean, ess_var = compute_vals(ess_points)
hmc_mean, hmc_var = compute_vals(hmc_points)
ess_values = np.hstack([ess_mean, np.repeat(["elss:"], 811)[:, np.newaxis], ess_var, x])
hmc_values = np.hstack([hmc_mean, np.repeat(["hmoc:"], 811)[:, np.newaxis], hmc_var, x])

mining_file = sys.argv[1]
mining_data = pd.read_csv(mining_file)
output_values = np.concatenate([mining_data.values.astype('|S32'), ess_values, hmc_values])
output_values = pd.DataFrame(output_values, columns=['m', 'model_sp', 'v', 'x'])
output_values.to_csv(mining_file, index=False)
