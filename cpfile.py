#!/usr/bin/python3
'''
Import the RMDup Module
'''
import rmdup
'''
Import the OS Operating System Functions Module 
'''
import os
'''
Give the user input for the file (It can be Absolute or Relative)
'''
INPUT = input("File to copy: ")
'''
Give the user output for the file name for the copy (It can be Absolute or Relative)
'''
OUTPUT = input("Name of Copy: ")
'''
Run RMDup's File Duplicator With The Input and Output files
'''
rmdup.CopyFile(INPUT,OUTPUT)
