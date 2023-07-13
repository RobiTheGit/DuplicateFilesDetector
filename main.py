#!/usr/bin/python3
# NOTE: Large directories will take a longer time to scan than smalelr ones
import hashlib
import os
import re
from sys import argv
import sys
global ext
global cmdName

if sys.platform.startswith("win32") or sys.platform.startswith('cygwin'):
    ext = 'bat'
    cmdName = "del"
else:
    ext = 'sh'
    cmdName = "rm"

global Dirs
try:
    script, RMPATH = argv
    
except:
    RMPATH = os.getcwd()
    
global DuplicateFiles
DuplicateFiles = {}
Dirs = sorted(os.listdir(RMPATH))

def FindDuplicate(SupFolder):
    DuplicateFiles = {}
    for file_name in Dirs:
        path = os.path.join(RMPATH, file_name)
        file_hash = Hash_File(path)
        
        if file_hash in DuplicateFiles:
           DuplicateFiles[file_hash].append(file_name)	#Add a filename to the list for the hash
        else:
            DuplicateFiles[file_hash] = [file_name]	#Make a list for the hash

    return DuplicateFiles

def Join_Dictionary(dict_1, dict_2):
    for key in dict_2.keys():
        if key in dict_1:
            pass	# Keeps Us from having 4 or more of the same file in a list
        else:
            dict_1[key] = dict_2[key]



def Hash_File(path):  
    try: 
        BinFile = open(path, 'rb')
        hasher = hashlib.md5()	#MD5 because it has way smaller hashes, making it easier to work with
        BUFFER_SIZE=65536		#Buffer size, 64 Kilobits
        buf = BinFile.read(BUFFER_SIZE)	#Read as much of the file as the buffer_size will allow the system to at once
        while len(buf) > 0:
            hasher.update(buf)
            buf = BinFile.read(BUFFER_SIZE)
        BinFile.close()
        return hasher.hexdigest()

    except:
        pass
def GenerateSH():
    try:
        Shell = open(f"RMDup.{ext}", "x")
    except:
        Shell = open(f"RMDup.{ext}", "w")
 
    for key in files:
        print(key)
        x = 0
        while x != len(files[key]):
            print(f"[{x}]",files[key][x])   
            x += 1

        Remove = input("Use the Numbers, or press Enter to Skip this one:\nWhich file would you like to Keep: ")
        try:
            Remove = int(Remove)
            del files[key][Remove]
            x = 0
            while x != len(files[key]):
                Shell.write(f'{cmdName} "{files[key][x]}"\n')
                x += 1
        except:
            pass
def Main():
    DuplicateFiles = {}
    temp = []
    for i in Dirs:  
        Join_Dictionary(DuplicateFiles, FindDuplicate(i))
        del DuplicateFiles[None]	#Delete Directories from the dictionary, we don't need to see those in the output
        results = DuplicateFiles	#The Duplicate files is the output result

            
    for key in results:
        if len(DuplicateFiles[key]) == 1:
           temp.append(key) 

    for x in temp: 
        del DuplicateFiles[x]
          
    if len(results) > 0:	#If we actually have any Duplicate files
        for key in results:
            print('['+key+ f']: Files with this hash: {len(DuplicateFiles[key])}')
            x = 0
            while x != len(DuplicateFiles[key]):
                print('['+DuplicateFiles[key][x]+']')
                x += 1
            print('\n')
            
        global files 
        files = DuplicateFiles
        GenerateSH()
    else:
        print("No Duplicate files")
Main()

