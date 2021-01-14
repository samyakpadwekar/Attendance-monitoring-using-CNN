# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:21:55 2019

@author: lenovo
"""

import os
# Function to rename multiple files
def main():
   i = 0
   path=r"C:\Users\lenovo\Desktop\major\123\5/"
   for filename in os.listdir(path):
      my_dest ="5_" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()