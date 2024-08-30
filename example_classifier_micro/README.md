Procedurally generate sets of images for training and evaluation:

```
gen_images.sh
```

Delete existing checkpoints (this usually happens automatically, but if code has changed, maybe not):
```
zapcpt.sh
```

Train model:
```
train.sh
```

You should press `^c` to stop streaming the logging output, otherwise subsequent commands will be ignored.

Evaluate the model:
```
inf.sh
scredit inference_results
```



** Progress


```
example_classifier_micro] ../driver.py train project classifier &
[2] 94397
example_classifier_micro] Traceback (most recent call last):
  File "/Users/home/github_projects/ml/example_classifier_micro/../driver.py", line 10, in <module>
    from pycore.base import *
  File "/Users/home/github_projects/ml/pycore/base.py", line 8, in <module>
    import jstyleson   # pip install jstyleson
    ^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'jstyleson'
```
