# Notes

## General
* Dynamically typed - Determined at runtime and retained thereafter unless reassigned to some other type.
* 

## DataTypes
* List - Can contains items of different types. For example can have int and string in the same list.
    * Indexing is 2 ways - negative and positive. Example: For a list of 3 values - 0,1,2,-1,-2,-3 are the valid 
index where list[2] == list[-1]
    * It also support sublist (slicing) access. Example: list[0:2] => includes value at index 0 and 1. It excludes upper 
    bound. Also support negative slicing. Example: list[-2:-1] 
        * Note: Slicing is only supported in Left -> Right direction. That means the values must be in increasing order 
        for slicing 
* Tuple - Immutable List
* Dict - Dictionary aka Map

## Modules and Packages
Python have modules, packages and libraries which can be imported in python ode.

## System Commands
Execute this on python command line to get details. 
* `dir(__builtins__)` - Gives you the details built in (internal) functions, errors, packages available from python
* `help(<functionName>)` - Gives you the details of the function. Example: `help(len)`
* `dir(list)` - Will give you all the methods applicable to list
* `dir(str)` - Will give you all the methods applicable to a string
* `os.__file__` - os is a module/package and this command will give us the location of the file for this module 

## Commands/Keywords Learned
* def
* print
* open()
* input()
* file.read(), readlines(), write(), close()
* str.splitLines()
* if else, if elif else
* while
* int()
* str()
* import glob2, os, sqllite3
* from datetime import datetime
* date.now(), date.strptime, date.strftime
* list - [a ,b ,c], list indexing
* tuple - Immutable List
* dictionary - {"k","v"}
* dir()
* help()