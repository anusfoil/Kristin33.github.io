#run this in any directory add -v for verbose 
#get Pillow (fork of PIL) from pip before running --> pip install Pillow

import os
import sys
from PIL import Image

def compressMe(file, quality=85, type="PNG"):
    filepath = os.path.join(os.getcwd(), file)
    oldsize = os.stat(filepath).st_size
    picture = Image.open(filepath)
    dim = picture.size

    if oldsize > 8000000:
        quality = 20
    elif oldsize > 5000000:
        quality = 40
    elif oldsize > 3000000:
        quality = 55
    elif oldsize > 1000000:
        quality = 70
    
    #set quality= to the preferred quality. 
    #I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
    picture.save("compressed_"+file, type, optimize=True, quality=quality) 
    
    newsize = os.stat(os.path.join(os.getcwd(),"Compressed_"+file)).st_size
    percent = (oldsize-newsize)/float(oldsize)*100
    print("File compressed from {} to {}".format(oldsize, newsize))
    # print "File compressed from {} to {} or {}".format(oldsize,newsize,percent)
    return percent

def main():

    folder = "photo"

    if len(sys.argv) > 1:
        compressMe(sys.argv[1], quality=sys.argv[2])
        print("Done")
        return 

    for file in os.listdir(folder):
        if not os.path.isfile("compressed_"+"{}/{}".format(folder, file)):
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', ".JPG"):
                compressMe("{}/{}".format(folder, file))
            if os.path.splitext(file)[1].lower() in ('.png'):
                compressMe("{}/{}".format(folder, file), type="PNG")
    print("Done")

if __name__ == "__main__":
    main()