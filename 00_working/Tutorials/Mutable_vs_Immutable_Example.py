#%%
# Immutable data types


def store_lower(_dict, _string):
    """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
    orig_string = _string
    _string = _string.lower()
    _dict[orig_string] = _string


d = {}
s = "Hello"

print(store_lower(d, s))

# %%

_string = "Hello"
_string = _string.lower()
print(_string)

_string = "Hi"
print(_string)


# %%
