def _init():
  global _global_dict
  _global_dict = {}

def set(name, value):
  _global_dict[name] = value

def get(name, default_value = None):
  try:
    return _global_dict[name]
  except KeyError:
    return default_value
    