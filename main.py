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
 
    for file_hash in files:
        print(file_hash, "\n")
        x = 0
        while x != len(files[file_hash]):
            print(f"[{x}]",files[file_hash][x],"\n")   
            x += 1

        Remove = input("Use the Numbers, or press Enter to Skip this one:\nWhich file would you like to Keep:\n> ")
        try:
            Remove = int(Remove)
            del files[file_hash][Remove]
            x = 0
            while x != len(files[file_hash]):
                Shell.write(f'{cmdName} "{files[file_hash][x]}"\n')
                x += 1
        except:
            pass
def Main():
    DuplicateFiles = {}
    temp = []
    for i in Dirs:  
        Join_Dictionary(DuplicateFiles, FindDuplicate(i))
        try:
           del DuplicateFiles[None]	# Delete Directories from the dictionary, we don't need to see those in the output, and they are none type
        except:
           pass

    for file_hash in DuplicateFiles:
        if len(DuplicateFiles[file_hash]) == 1:
           temp.append(file_hash) 

    for x in temp: 
        del DuplicateFiles[x]
          
    if len(DuplicateFiles) > 0:	#If we actually have any Duplicate files
        for file_hash in DuplicateFiles:
            print('['+file_hash+ f']: Files with this hash: {len(DuplicateFiles[file_hash])}')
            x = 0
            while x != len(DuplicateFiles[file_hash]):
                print('['+DuplicateFiles[file_hash][x]+']')
                x += 1
            print('\n')
            
        global files 
        files = DuplicateFiles
        GenerateSH()
    else:
        print("No Duplicate files")
Main()
