# Troubleshooting

## `np.bool` is deprecated

### Reason

Theano is outdated.

### Fix

In `...\site-packages\theano\scalar\basic.py`, change the line that says:

```
self.ctor = getattr(np, o_type.dtype)
```

to

```
self.ctor = o_type.dtype
```

## AttributeError: module 'numpy.distutils.__config__' has no attribute 'blas_opt_info'

### Reason

Theano is outdated

### Fix

In ..`\site-packages\theano\link\c\cmodule.py`, change the line that says:

```
blas_info = numpy.distutils.__config__.blas_opt_info
```

to

```
blas_info = np.distutils.__config__.blas_ilp64_opt_info
```

## AttributeError: module 'numpy' has no attribute 'int'.

### Reason

skopt

### Fix

In `...\Lib\site-packages\numpy\__init__.py` change the line that says:

```
return np.round(X_orig).astype(np.int)
```

to

```
return np.round(X_orig).astype(int)

```
