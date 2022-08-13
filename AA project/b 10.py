from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['figure.figsize'] = [5,5]
plt.rcParams.update({'font.size':18})

A = imread(os.path.join('--','DATA','national.jpg'))
B = np.mean(A, -1);
pit.figure()
pit.imshow(256-A)
pit.axis('off')
  
