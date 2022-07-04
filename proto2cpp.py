import os
import sys
import re
import fnmatch
import inspect

class proto2cpp:

  ## Logging level: do not log anything.
  logNone   = 0
  ## Logging level: log errors only.
  logErrors = 1
  ## Logging level: log everything.
  logAll    = 2

  ## Constructor
  #
  def __init__(self):
    ## Debug log file name.
    #self.logFile = "proto2cpp.log"
    ## Error log file name.
    #self.errorLogFile = "proto2cpp.error.log"
    ## Logging level.
    print(f'self.logNone={self.logNone}')
    self.logLevel = self.logNone  # ←なんかこれがあると README.md の内容がおかしくなるっぽい

  ## Handles a file.
  ##
  ## If @p fileName has .proto suffix, it is processed through parseFile().
  ## Otherwise it is printed to stdout as is except for file \c proto2cpp.py without
  ## path since it's the script given to python for processing.
  ##
  ## @param fileName Name of the file to be handled.
  #
  def handleFile(self, fileName):
    if not fnmatch.fnmatch(filename, os.path.basename(inspect.getfile(inspect.currentframe()))):
        with open(filename, 'r') as theFile:
          output = ''
          for theLine in theFile:
            output += theLine
          print(output)


converter = proto2cpp()
# Doxygen will give us the file names
for filename in sys.argv:
  print(f'filename={filename}')
  converter.handleFile(filename)

# end of file
