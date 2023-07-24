#!/usr/bin/python3
# NOTE: Large directories will take a longer time to scan than smaller ones, but not nearly as long as it used to
# This is not recurssive, and if it was, you'd be waiting days for it to finish unless you main and sub-directories were really small
# 
# RMDup, Remove Duplicate Files
#
# RobiTheGit, 2023
#
# This searches for duplicate files, then outputs them in a nice fashion, asks you what you want to keep, and after generating a script,
# asks you if you want to delete them, and if you enter "y" (not case-sensitive), deletes them
#
# Also, you can make duplicate files
#

import hashlib
import os
import re
from sys import argv
import sys
import shutil
global ext
global cmdName
global cmdtorun
#	Define any system specific variables
if sys.platform.startswith("win32") or sys.platform.startswith('cygwin'):
    ext = 'bat'
    cmdName = "del"
    cmdtorun = "RMDup.bat"
else:
    ext = 'sh'
    cmdName = "rm"
    cmdtorun = "./RMDup.sh"
global Dirs
if __name__ == "__main__":
    try:
        script, RMPATH = argv
 
    except:
        RMPATH = os.getcwd()



global DuplicateFiles
DuplicateFiles = {}


class RemoveDuplicates(object):
# This is the code that finds duplicate files
# We start wiht an empty dictionary to fill with file hashes, and a list of files that use that hash
# We call to hash the file in RMDup_Hash_File() with the path being RMPATH, the directory to search, and the file name

    def RMDup_FindDuplicate(SupFolder):
        DuplicateFiles = {}
        for file_name in Dirs:
            path = os.path.join(RMPATH, file_name)
            file_hash = RemoveDuplicates.RMDup_Hash_File(path)

            if file_hash in DuplicateFiles:
               DuplicateFiles[file_hash].append(file_name)	#Add a filename to the list for the hash
            else:
                DuplicateFiles[file_hash] = [file_name]	#Make a list for the hash

        return DuplicateFiles

# This is the code to join the dictionaries together to show the duplicate files
# We pass when the key is in dict 1 to avoid not only having 4 of each file in a dictionary, but also to let the code later remove files that don't have duplicates
# Otherwise, we merge those dictionaries

    def RMDup_Join_Dictionary(dict_1, dict_2):
        for key in dict_2.keys():
            if key in dict_1:
                pass	# Keeps Us from having 4 or more of the same file in a list
            else:
                dict_1[key] = dict_2[key]

# This is the function to get the MD5 file hash for testing what files are duplicates
# We open the file that is being read in RMDup_FindDuplicate() with read-binary mode, and with the variable name BinFile
# We set our hasher method to MD5, Message-Digest Algorithm 5, hashing since it has pretty small hashes, making it a bit easier to work with
# The buffer size is 8000000 Kilobits, which is 1 Gigabyte, so most machines should be able to run it, but some older hardware may not be able to run it
# We multiply it by 1024 to make it work in the code, and so it is a lot easier for me, Robi, to change

    def RMDup_Hash_File(path):  
        try: 
            with open(path, 'rb') as BinFile:
                hasher = hashlib.md5()	#MD5 because it has way smaller hashes, making it easier to work with
                BUFFER_SIZE=8000000		#Buffer size, 8000000 Kilobits, or 1 Gigabyte
                buf = BinFile.read(BUFFER_SIZE*1024)	#Read as much of the file as the buffer_size will allow the system to at once
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = BinFile.read(BUFFER_SIZE*1024)
                BinFile.close()
                return hasher.hexdigest()
        except:
            pass

# This is the code to generate shell or batch scripts fopr deleting the files, as well as actually deleting the files if you choose to do so
# The function name is a bit of a misnomer since it doesn't just generate shell scripts anymore, however, when I originally worte the function, I only hade Posix systems in mind
# We create or open the file, and if we are on linux, give permission to execute it, then ask for input of which file to keep, which you can skip and keep alll of them if you'd like
# Then we ask for input we we have finished writing the entire script if they want to delete the files, all this really does is exceute the scipt we generated

    def RMDup_GenerateSH():

        try:	#Try to make RMDup.bat/sh
            Shell = open(f"RMDup.{ext}", "x")
            if ext == "sh":
                os.system("chmod +x RMDup.sh")

        except:	#if it exists, just overwrite the file
            Shell = open(f"RMDup.{ext}", "w")
            if ext == "sh":
                os.system("chmod +x RMDup.sh")

        for file_hash in files:
            print(file_hash, "\n")
            x = 0
            while x != len(files[file_hash]):
                print(f"[{x}] {files[file_hash][x]}\n")   
                x += 1

            Remove = input("Use the Numbers, or press Enter to Skip this one:\nWhich file would you like to Keep:\n> ")
            try:
                Remove = int(Remove)
                del files[file_hash][Remove]
                x = 0
                while x != len(files[file_hash]):
                    DupFilePath = f'"{RMPATH}/{files[file_hash][x]}"'
                    Shell.write(f'{cmdName} {DupFilePath}\n')
                    x += 1
            except:
                pass
        Choice = input('Delete files now? [y/N]:\n> ')
        if Choice.upper().startswith("Y"):
            Shell.close()
            os.system(cmdtorun)
        else:
            if __name__ == "__main__":
                sys.exit(0)
            else:
                pass

# The main function, and the one you call to run this outside of this script
# it clears our lists and dictionaries for us
# This is really just a handler to run all of the functions inside the RemoveDuplicates class
# It also prints out the duplicate files, or tells the user if there aren't any
# From our DuplicateFiles dictionary, we delete directories or files that aren't duplicates here


def RMDup(Directory):
    global Dirs
    if not __name__ == '__main__':
        global RMPATH
        RMPATH = Directory
        Dirs = Directory
        Dirs = sorted(os.listdir(Directory))    
 
    DuplicateFiles = {}
    temp = []
    for i in Dirs:  
        RemoveDuplicates.RMDup_Join_Dictionary(DuplicateFiles, RemoveDuplicates.RMDup_FindDuplicate(i))
        try:
           del DuplicateFiles[None]	# Delete Directories from the dictionary, we don't need to see those in the output, and they are none type
        except:
           pass

    for file_hash in DuplicateFiles:
        if len(DuplicateFiles[file_hash]) == 1:
           temp.append(file_hash) 

    for x in temp: 
        del DuplicateFiles[x]
        
    print(f"Duplicate files in: {RMPATH}/")
    if len(DuplicateFiles) > 0:	# If we actually have any Duplicate files
        for file_hash in DuplicateFiles:
            print(f'[{file_hash}]: Files with the hash: ({len(DuplicateFiles[file_hash])})')
            x = 0
            while x != len(DuplicateFiles[file_hash]):
                print(f'[{DuplicateFiles[file_hash][x]}]')
                x += 1
            print('\n')
            
        global files 
        files = DuplicateFiles
        RemoveDuplicates.RMDup_GenerateSH()
    else:
        print(f"No Duplicate files in: {RMPATH}/")

def CopyFile(INPUT, OUPUT):
    shutil.copyfile(INPUT, OUPUT)
def GetHash(INPUT):
    with open(INPUT, 'rb') as BinFile:
        hasher = hashlib.md5()	#MD5 because it has way smaller hashes, making it easier to work with
        BUFFER_SIZE=8000000		#Buffer size, 8000000 Kilobits, or 1 Gigabyte
        buf = BinFile.read(BUFFER_SIZE*1024)	#Read as much of the file as the buffer_size will allow the system to at once
        while len(buf) > 0:
            hasher.update(buf)
            buf = BinFile.read(BUFFER_SIZE*1024)
        BinFile.close()
        print(hasher.hexdigest()) 
          
if __name__ == "__main__":
    Dirs = sorted(os.listdir(RMPATH))
    RMDup(Dirs)
