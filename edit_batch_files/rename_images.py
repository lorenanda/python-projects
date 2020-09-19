# code to rename multiple images in a folder

import os

def main():
   i = 0

   #location of the images to be renamed
   path = "./rename_files/"
   for filename in os.listdir(path):

      #rename images as Screenshot_number.png
      my_dest = "Screenshot_" + str(i) + ".png"
      my_source = path + filename
      my_dest = path + my_dest

      os.rename(my_source, my_dest)

      #increase the number in the name for each image
      i += 1

# driver code
if __name__ == '__main__':
   main()