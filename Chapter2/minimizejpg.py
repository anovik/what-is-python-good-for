import os
from PIL import Image
  
def compressJpeg(file):   
    filepath = os.path.join(os.getcwd(), 
                            file)
                            
    print(os.path.getsize(filepath)    
                            
    picture = Image.open(filepath)   
   
    picture.save("compressed_" + file, 
                 "JPEG", 
                 optimize = True, 
                 quality = 80)
                 
    newFilePath = os.path.join(os.getcwd(), 
                            "compressed_" + file)
                            
    print(os.path.getsize(newFilePath)    
    return
    
currentdir = os.getcwd()
  
formats = ('.jpg', '.jpeg')
  
for file in os.listdir(currentdir):        
    if os.path.splitext(file)[1].lower() in formats:         
        compressJpeg(file)