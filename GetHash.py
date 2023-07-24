#!/usr/bin/python3
'''
Import the RMDup Module
'''
import rmdup
'''
Give the user input for the file (It can be Absolute or Relative)
'''
INPUT = input("File to Get Hash of: ")
'''
Run RMDup's File Hash Finder
'''
rmdup.GetHash(INPUT)
