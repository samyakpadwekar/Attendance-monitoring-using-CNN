import cv2
import os
import glob
from IPython import display
from PIL import Image
import numpy as np
from keras.preprocessing import image
img_dir = r"C:\Users\lenovo\Desktop\test" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
d=0
import numpy as np
array= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for f1 in files:
    im = cv2.imread(f1)    
    filename = "%d.jpg"%d
    test_img = image.load_img(filename,target_size=(256,256))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis = 0)
    result = classifier.predict_classes(test_img)
    result_prob = classifier.predict_proba(test_img)
    result_predict = classifier.predict(test_img)
    array[result]=1
    d+=1  
p=array.tolist()
print(type(array))