import sys
import inspect
import re
import os.path

class _LocalVars:
  """
  This class is used to produce an instance to hold the tools' local variables
  """
  def __init__(self):
      self.prevTime = -1
      self.rxFilenameOnly = re.compile(".*/([^/]*)$")
      self.repMap = set()

# Construct a singleton instance for the static variables
_v = _LocalVars()


def pr(fmt='\n', *args):
  """Debug printing of string with % formatting, and accompanying arguments"""
  sys.stdout.write(fmt % args)

def sprintf(fmt, *args):
  v = fmt % args
  return v

def d(s):
  """
  Convert an object to a string (by calling str(x)), or returns '<None>' if
  object is None
  """
  if s is None:
    return  "<None>"
  if type(s) is unicode:
    return unicodeToStr(s)
  return str(s)

def dtype(s):
  """
  Print string representation of object (with d(x)), followed by type name
  """
  if s is None:
    return '<None>'
  else:
    return d(s) + " (type=" + str(type(s)) + ")"

def simple_name(filename, line):
    """    Builds a nice string from a pathname and line number; removes directories from pathname.  """
    m = _v.rxFilenameOnly.match(filename)
    if m:
        filename = m.group(1)
    return "(" + filename.ljust(12) + str(line).rjust(4) + ")"

def warn_skip(nSkip, *args):
  """Prints warning, if hasn't yet been printed."""
  loc = get_caller_location(nSkip + 2)
  s = "*** warning " + loc + ": "
  if len(args):
      msg = s + args[0] % args[1:]
  else:
      msg = s

  if not msg in _v.repMap:
      _v.repMap.add(msg)
      print(msg)

def warn(*args):
  warn_skip(1, *args)

def get_caller_location(nSkip=2):
  h = inspect.stack()
  if  0 <= nSkip < len(h):
    fi = h[nSkip]  # inspect.getframeinfo(h[1])
    loc = simple_name(fi[1], fi[2])  # fi.__file__,fi.f_lineno)
  else:
    loc = "(UNKNOWN LOCATION)"
  return loc

def unimp(*args):
  """Prints unimplemented msg, if hasn't yet been printed."""
  loc = get_caller_location()
  s = "*** unimplemented " + loc + ": "
  if len(args):
      msg = s + args[0] % args[1:]
  else:
      msg = s

  if not msg in _v.repMap:
      _v.repMap.add(msg)
      print(msg)

def my_assert(cond):
  warn_skip(1, "checking assertion")
  error_if(not cond)

def error(msg=None):
  """
  Raise an exception, optionally with a message
  """
  if msg is None:
    msg = "error occurred"
  raise Exception(msg)

def error_if(cond, msg=None):
  """
  Raise an exception, optionally with a message, if a condition is true
  """
  if cond:
    error(msg)

def current_dir():
  """
  Get absolute path of current directory, as unicode string
  """
  return os.path.abspath(unicode(os.curdir))
