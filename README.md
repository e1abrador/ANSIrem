# ANSIrem

ANSIrem will remove all ANSI characters on a given text file (updating the same file, not creating a new one), for example:

````none
$ cat results.txt
^[[92mtest.example.com^[[0m^[[94m
$ python3 ASNIrem.py results.txt
$ cat results.txt
test.example.com
````

# Why ANSIrem?

Crafted to tackle the inconvenience caused by certain tools (such as httpx, amass, and others) that output results with distracting colors. No longer will you need to rerun workflows or add additional flags to adjust the output. With this script, seamless workflow is just a click away.
