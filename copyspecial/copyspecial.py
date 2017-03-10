#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_files(dir):
    filenames = os.listdir(dir)
    paths = []
    for filename in filenames:
        match = re.search(r'__\w+__', filename)
        if match:
            path = os.path.join(dir, filename)
            abspath = os.path.abspath(path)
            paths.append(abspath)
    return paths

def to_directory(files, destination):
    destpath = os.path.abspath(destination)
    mkdir_cmd = 'mkdir ' + destpath
    (status, output) = commands.getstatusoutput(mkdir_cmd)
    if status:
        sys.stderr.write('there was an error: ' + output)
        sys.exit(1)

    for f in files:
        cp_cmd = 'cp ' + f + ' ' + destpath
        (st, op) = commands.getstatusoutput(cp_cmd)
        if st:
            sys.stderr.write('there was an error: ' + op)
            sys.exit(1)
    return

def to_zip(files, destination):
    destpath = os.path.abspath(destination)
    zip_cmd = 'zip -j ' + destpath + ' ' + ' '.join(files)
    (status, op) = commands.getstatusoutput(zip_cmd)
    if status:
        sys.stderr.write('there was an error: ' + output)
        sys.exit(1)
    return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  if args[0] == '--todir' and len(args) == 3:
      source = args[1]
      destination = args[2]
      files = get_files(source)
      to_directory(files, destination)
      return

  if args[0] == '--tozip' and len(args) == 3:
      source = args[1]
      destination = args[2]
      files = get_files(source)
      to_zip(files, destination)
      return

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  print get_files(args[0])
  return

if __name__ == "__main__":
  main()
