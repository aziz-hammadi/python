def ft_filter(function, iterable):
    ft_filter.___doc___ = ```Construct an iterator from those elements of iterable for which function is true. iterable may be either a sequence, a container which supports iteration, or an iterator. \nIf function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.```
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
