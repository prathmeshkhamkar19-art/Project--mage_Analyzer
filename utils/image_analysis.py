import numpy as np
from PIL import Image




def image_analysis(path):    # get the path in function after call this 
    img = Image.open(path)   #open the image using pil function image.open()
    img_array =np.array(img)  #convert to array using np(numpy)
    width , height = img_array.shape[:2]
    data = {
      "shape":img_array.shape,
      "Brightness":img_array.mean(),
      "Resolution":  (width,height)
    }
    return data   #return the dictionary
    
