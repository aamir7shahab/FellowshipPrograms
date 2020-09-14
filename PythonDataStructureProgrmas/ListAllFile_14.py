# 14. Write a Python program to list all files in a directory in Python.

from subprocess import call
call("ls", shell=True)
