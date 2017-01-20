# Experiments

## Install Markdown extension for Chrome browser

This file, for example, is a 'markdown' file, which is a type of markup (like html) but easier to use.

If you're using Chrome, install this extension to allow you to view these files within Chrome:

https://chrome.google.com/webstore/detail/markview/ehnambpmkdhopilaccgfmojilolcglhn


## Verifying python exists

```
ml> python --version
Python 2.7.10
```

```
ml> python py/quicksort.py
pivot 10 left [3, 6, 8, 1, 2, 1] right []
pivot 1 left [] right [3, 6, 8, 2]
pivot 8 left [3, 6, 2] right []
pivot 6 left [3, 2] right []
pivot 2 left [] right [3]
[1, 1, 2, 3, 6, 8, 10]
ml>
```

## Installing additional packages 'scipy', 'numpy'


```
py> which pip
/usr/local/bin/pip

py> python -m pip install --upgrade pip
Requirement already up-to-date: pip in /usr/local/lib/python2.7/site-packages

py> pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose Pillow

Collecting matplotlib
  Downloading matplotlib-2.0.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (12.8MB)
    100% |████████████████████████████████| 12.8MB 92kB/s
Collecting ipython
  Downloading ipython-5.1.0-py2-none-any.whl (747kB)
    100% |████████████████████████████████| 747kB 1.1MB/s
  etc
  etc
  etc
  :
  :

```


Now it seems to do something...

```
py> python cat.py
uint8 (196, 236, 3)
py>
```

