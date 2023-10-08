# ANSIrem

ANSIrem will remove all ANSI characters on a given text file (updating the same file, not creating a new one), for example:

````none
$ cat results.txt
^[[92mtest.example.com^[[0m^[[94m
$ python3 ASNIrem.py results.txt
$ cat results.txt
test.example.com
````
