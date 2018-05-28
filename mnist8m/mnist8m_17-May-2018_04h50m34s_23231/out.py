import pandas as pd
import numpy as np
d = pd.read_csv("predictions.csv").as_matrix()
true = d[:, :10]
pred = d[:, 10:20]
true = np.argmax(true, axis=1)
pred = np.argmax(pred, axis=1)
print(np.sum(true == pred))
