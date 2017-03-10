#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import os
import commands

# Define a main() function that prints a little greeting.
def List(dir):
  # Get the name from the command line, using 'World' as a fallback.
  cmd = 'ls -l ' + dir
  (status, output) = commands.getstatusoutput(cmd)
  if status:
      sys.stderr.write('there was an error:' + output)
      sys.exit(1)
  print output

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  List(sys.argv[1])
