import os
import PIL
from PIL import Image
  
def resizeJpeg(file):   
    filepath = os.path.join(os.getcwd(), 
                            file)
                            
    print(os.path.getsize(filepath))    
                            
    picture = Image.open(filepath)   

    resizedHeight = 500

    hpercent = (resizedHeight / float(picture.size[1]))
    newWidth = int((float(picture.size[0])*float(hpercent)))
    img = picture.resize((newWidth, resizedHeight), Image.LANCZOS)
      
    img.save("resized_" + file)
                 
    newFilePath = os.path.join(os.getcwd(), 
                            "resized_" + file)
                            
    print(os.path.getsize(newFilePath))    
    return
    
currentdir = os.getcwd()
  
formats = ('.jpg', '.jpeg')
  
for file in os.listdir(currentdir):        
    if os.path.splitext(file)[1].lower() in formats:         
        resizeJpeg(file)
