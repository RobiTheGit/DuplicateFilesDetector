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
Run RMDup's Duplicate File Detector in the Current Working Directory, the function must have absolute paths
'''
rmdup.RMDup(os.getcwd())
