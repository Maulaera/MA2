# Requirements
  * Python 3+ (I'm running Python 3.10.12)

> This code makes use of the 'f"..." syntax. 
> This syntax was introduced in Python 3.6

# Sample execution & Output

This code, per assignment requirements, must be ran with command line
arguments. 

If run without command line arguments, using
```
./main.py 
```
The following usage message will be displayed.
```
Usage: ./main.py <base> <decimal1> <decimal2> <decimal3>
```
If run using
```
./main.py 2 0.5 0.25 0.75

output similar to

```
| Base 10 | Base 2 |
| :-------| :--------|
| 0.5     | 0.1      |
| 0.25    | 0.0;1    |
| 0.75    | 0.1;1    |
```
will be generated. Note that the border lines may vary dependant on CL input.