# Importing Required Modules 
from rembg import remove 
from PIL import Image 
  
# Store path of the image in the variable input_path 
input_path =  "E:/Ijass/OA_PY_AUG_9.30-10.30/images/minion.jpg" 
  
# Store path of the output image in the variable output_path 
output_path = "E:/Ijass/OA_PY_AUG_9.30-10.30/images/output/minion.png"
  
# Processing the image 
input = Image.open(input_path) 
  
# Removing the background from the given Image 
output = remove(input) 
  
#Saving the image in the given path 
output.save(output_path) 