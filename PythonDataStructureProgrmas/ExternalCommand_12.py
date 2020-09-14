# 12. Write a python program to call an external command in Python.

from subprocess import call
call("echo Hello World", shell=True)
call("pwd", shell=True)
call("ls -l", shell=True)

