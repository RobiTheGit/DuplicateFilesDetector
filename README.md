# DuplicateFilesDetector
Large Directories May Take a Long Time To Scan.

Running:

scan a specific directory

`python3 main.py {directory_to_scan}`

scan the current directory

`python3 main.py`

you can replace `python3` with `./` on linux since there is a shebang

The output will only list files that have the same hash, and no single files

Example:

```
ad5678997cade8869e64a90cded854fa
['Rom.bin', 'Rom2.bin']
```

if there are no duplicate files, it'll print `No Duplicate files`

IF you have dupliicates, it'll ask you which one you want to Keep and delete the others, answer with an interger, because otherwise, it'll skip it

It writes it into a shell script, so it won't delete the files until you run the shell script

Tool is for Linux/Mac only
