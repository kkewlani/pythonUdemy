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
* Exception Handling - try... except

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
### type 
Used to get the type of a variable :
```
>>> val = 10.1
>>> type(val)
<class 'float'>
``` 
### Data Types
int, float, str, list 
List Example: 
```
>>> vals = [12, "akjshd", 12.1, "1"]
>>> print (vals)
[12, 'akjshd', 12.1, '1']

```
You can also use range with lists. Example:
Following has a step of 3 - skipping 2 numbers in between aka a series/pattern 
```
>>> list(range(1, 10,3))
[1, 4, 7]

```

There can also be lists of lists.

### dir n help
_'dir'_ Provides the details of all the possible methods that can be executed on a specific type.
example:
```
>>> dir(float)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', 
'__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', 
'__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
'__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 
'fromhex', 'hex', 'imag', 'is_integer', 'real']
``` 
_'help'_ provides the description on the type as well as the specific method/operation associated with a type.
_'help'_ is the Documentation provider, somewhat equivalent of _man_ for linux commands
Example:
```
>>> help(str.upper)
Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.

```
### Built-in Features 
**'print'** is a function and not a method and thus not attached to a specific type. It works with different data types.
This is one of the built in feature of python. 
To get details on other built in provided features you can run following cmd:
```
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 
'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 
'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 
'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', 
'__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 
'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 
'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 
'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

```
The ones with **__** are the ones that are used by Python internally and might noe be used as frequently by programmers.

 There are other libraries that provide more features/functionalities. those can also be explored in similar ways. 
 Example: 
```
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

```
### dictionary
Dictionary is equivalent to a map - a key, value pair.
Example:
```
>>> grades = {"kevin": 9.2, "Brian": 9.0}
>>> dir(grades)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> grades.values()
dict_values([9.2, 9.0])
>>> grades.keys()
dict_keys(['kevin', 'Brian'])

```
### Tuple
A list with parenthesis _()_ instead of square brackets _[]_ . However there are some differences in how these are
processed. Tuples are immutable whereas lists are mutable
Example:
```
>>> t = (  2, "4", 5)
>>> l = [ 2, "4", 5]
>>> l.append(6)
>>> t.append(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> l.remove("4")
>>> print(l)
[2, 5, 6]
>>> t.remove("4")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'

```

### Lists
Lists are the group of data. The data types can be same across or can be different,
Example:
```
>>> vals = [12, "akjshd", 12.1, "1"]
>>> print (vals)
[12, 'akjshd', 12.1, '1']

```
Lists store index as well.
Example:
```
>>> print(l)
[2, 5, 6, 4, 7]

>>> l.index(6)
2

>>> help(list.index)

index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.

```

Index position can be provides as input while traversing the list
Example:
```
>>> l.append(2)
>>> print(l)
[2, 5, 6, 4, 7, 2]
>>> l.index(2, 3)
5
>>> l.index(2)
0
>>> l.index(2,1,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 2 is not in list
>>> 

```
Lists have a positive as well as a negative index
Example:
```
>>> l[0]
2
>>> l[-5]
5
>>> l[-6]
2
```
Lists can be traversed by providing the ranges instead of index in the above
Example:
l[start:NonInclusiveEnd]
```
>>> print(l)
[2, 5, 6, 4, 7, 2]
>>> l[1:4]
[5, 6, 4]
```
range provided as input should be in increasing order
_`l[start:end]`_
Here _start_ should be <= _end_
Example:
```
>>> print(l)
[2, 5, 6, 4, 7, 2]
>>> l[-4:-5]
[]
>>> l[-4:-6]
[]
>>> l[4:2]


>>> l.remove(2)
>>> print(l)
[5, 6, 4, 7, 2]
>>> l[-1]
2
>>> l[-6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> l[-5]
5
>>> l[-5:-1]
[5, 6, 4, 7]
>>> l[-5:0]
[]
>>> l[-5:]
[5, 6, 4, 7, 2]


```


### Self
_self_ - implies the object/type itself
Example:
```
>>> help(list.append)
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

```
Here _self_ refers to the list itself and the ```append``` function takes only one argument.
Example:
```
>>> print(l)
[2, 5, 6]
>>> l.append(4)
>>> print(l)
[2, 5, 6, 4]
```

### Files



* def
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
* zip - to be used with for loop having multiple variables iterating on multiple ranges
* tuple - Immutable List
* dictionary - {"k","v"}

* help()
* with - Example: ```with open("myFile", "w") as myfile:``` will take care of closing the resources once the with block 
finishes and even take care of it in case of exceptions/errors
* [] - Used for defining a Tuple
* () - Used for defining a List
* {} - Used for defining a dictionary
* try... except - ```try: ... except [exceptionName]: ...```


## Useful Modules
* datetime - ```from datetime import datetime```. Some cmds - ```datetime.now() ```
    * strftime("<format>") - for creating custom format can use the different Data formatting COdes used in python
    

## Date Format Table

## Abbreviations/Syntax/Glossary
* [value] - Square brackets in notes means that value is optional