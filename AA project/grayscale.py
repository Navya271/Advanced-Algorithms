from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['figure.figsize'] = [5,5]
plt.rcParams.update({'font.size':18})

A = imread(os.path.join('--','DATA','national.jpg'))
B = np.mean(A, -1); # covert RCB to grayscale
pit.figure()
pit.imshow(256-A) # cmap 'gray_r')
pit.axis('off')



Bt=np.fft.fft2(B)
Btsort=np.sort(np.abs(Bt.reshape(-1))) # sort by magnitude

#zero out of all small coefficient and inverse transform

for keep in (0.1, 0.05, 0.01, 0.002);
    thresh = Btsort[int(np.floor((1-keep)*len(Btsort)))]
    ind = np.abs(Bt)>thresh         #find small indices
    Btlow = Bt * ind                #threshold small indices
    Alow = np.fft.ifft2(Btlow).real  #compressed image
    plt.figure()
    plt.imshow(256-Alow,cmap='gray')
    plt.axis('off')
    plt.title('compressed image: keep=' + str(keep*100) + '%')

    
    








