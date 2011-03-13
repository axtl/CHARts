#!/usr/bin/env python

# # CHARts #
# Programmers love numbers. Numbers help shape things, turn amorphous blobs
# into definable structures. In that curiosity, I wrote myself a little utility
# for displaying the kinds of characters I use in source code. This isn't
# particularly useful for scientific work, except maybe for helping people
# decide which languages use more sigils, and if a particular language may
# increase the risks of RSI.

#
import getopt
import os
import sys


# Dictionary to store all of counted characters and their respective counts.
_chardict = {}

# The error code for incorrect arguments (number or type of)
ERR_ARGS = 1
# The error code for invalid arguments (non-existent paths)
ERR_INVALID = 2

# The main function of this program parses the arguments and triggers the
# per-folder and per-file counters, as appropriate.

def main(argv):
    # Parse command line arguments and set any flags as needed.
    try:
        opts, args = getopt.getopt(argv, 'h', ['help'])
    except getopt.GetoptError:
        usage()
        sys.exit(ERR_ARGS)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()

    # Look at each argument in the given list and decide if it needs to be
    # processed as a file or a folder.
    # Quit if any of the given paths does not exist.
    for elem in args:
        fullpath = os.path.abspath(os.path.expanduser(elem))
        if not os.path.exists(fullpath):
            sys.stderr.write('The specified path does not exist: %s' % elem)
            sys.exit(ERR_INVALID)
        if os.path.isdir(fullpath):
            count_folder(fullpath)
        else:
            count_file(fullpath)

# Print a helpful message to the user, informing of the various options the
# program understands.

def usage():
    sys.stdout.write('Usage:\n')
    sys.stdout.write('\t%s file_or_folder_1 <others ...>\n' % sys.argv[0])

# Count the number of characters in the given file.

def count_file(path):
    pass

# Walk the given folder and trigger a count of all the files encountered, then
# recurse into subfolders until the entire tree has been traversed.

def count_folder(path):
    pass


# Run the program.
if __name__ == '__main__':
    main(sys.argv[1:])
