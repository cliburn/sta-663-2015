"""
When this file is imported with `import foo`,
only `useful_func1()` and `useful_func()` are loaded, 
and the test code `assert ...` is ignored. However,
when we run foo.py as a script `python foo.py`, then
the two assert statements are run.
Most commonly, the code under `if __naem__ == '__main__':`
consists of simple examples or test cases for the functions
defined in the moule.
"""

def useful_func1():
    pass

def useful_fucn2():
    pass

if __name__ == '__main__':
    assert(useful_func1() is None)
    assert(useful_fucn2() is None)