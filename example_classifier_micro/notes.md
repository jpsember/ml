Now trying to get new mac mini working to perform training.


```
Starting training session at: Fri 5:04 PM (+35.0s)
3.9.6
Traceback (most recent call last):
  File "/Users/home/github_projects/ml/example_classifier_micro/../driver.py", line 13, in <module>
    from pycore.base import *
  File "/Users/home/github_projects/ml/pycore/base.py", line 8, in <module>
    import jstyleson   # pip install jstyleson
ModuleNotFoundError: No module named 'jstyleson'
```

I am having trouble installing `jstylejson`; so now trying something called `json-with-comments`
```
pip3 install json-with-comments
```

NOTE: why can't I type pip instead of pip3?

