# RMDup
Large Directories May Take a Long Time To Scan.

Tool is for is for Linux, Mac, and Windows

Running:

scan a specific directory

`python3 rmdup.py {directory_to_scan}`

scan the current directory

`python3 rmdup.py`

you can replace `python3` with `./` on linux since there is a shebang, and on windows, replace `python3` with `python`

to do the `./rmdup.py` method, you'll have to run `chmod +x rmdup.py`

The output will only list files that have the same hash, and no single files

Example:

```
ad5678997cade8869e64a90cded854fa

['Rom.bin']
['Rom2.bin']
```

if there are no duplicate files, it'll print `No Duplicate files`

IF you have dupliicates, it'll ask you which one you want to Keep and delete the others, answer with an interger, because otherwise, it'll skip it (you can use this to your advantage to skip files where you want to delete none)

It writes it into a shell or batch script, so it won't delete the files until you run the shell or batch script, but it'll ask you in the program if you want to delete them now, type "y" to do so, otherwise, it exits the program.

If you want, in the working directory of whatever code you are writing, you can include the code and in whatever you may be writing, add `import rmdup` and then call the code with `rmdup.RMDup(path)` with `path` being the path you want to use. See [randomscript.py](https://github.com/RobiTheGit/RMDup/blob/main/randomscript.py) for an example script
