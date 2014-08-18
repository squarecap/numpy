def _fastCopyAndTranspose(a):
    return a.T.copy()

def copyto(dst, src, casting='same_kind', where=None):
    if where is None:
        dst.fill(src)
    else:
        dst[where] = src

def format_longfloat(x, precision):
    return "%%.%df" % precision % x

def set_typeDict(d):
    pass

def may_share_memory(a, b):
    """
    Determine if two arrays can share memory

    The memory-bounds of a and b are computed.  If they overlap then
    this function returns True.  Otherwise, it returns False.

    A return of True does not necessarily mean that the two arrays
    share any element.  It just means that they *might*.

    Parameters
    ----------
    a, b : ndarray

    Returns
    -------
    out : bool

    Examples
    --------
    >>> np.may_share_memory(np.array([1,2]), np.array([5,8,9]))
    False

    """
    from ..lib import byte_bounds
    a_low, a_high = byte_bounds(a)
    b_low, b_high = byte_bounds(b)
    if b_low >= a_high or a_low >= b_high:
        return False
    return True

from _numpypy.multiarray import *

for name in '''
CLIP WRAP RAISE MAXDIMS ALLOW_THREADS BUFSIZE nditer nested_iters
broadcast empty_like fromiter fromfile frombuffer newbuffer getbuffer
int_asbuffer set_numeric_ops can_cast promote_types
min_scalar_type result_type lexsort compare_chararrays putmask einsum inner
_vec_string datetime_data
datetime_as_string busday_offset busday_count is_busday busdaycalendar
_flagdict flagsobj
'''.split():
    if name not in globals():
        globals()[name] = None