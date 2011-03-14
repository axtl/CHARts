#!/usr/bin/env python

# # CHARts #
# ## Count Code Characters ##
# Programmers love numbers. Numbers help shape things, turn amorphous blobs
# into definable structures. Because of curiosity, I wrote myself a little
# utility for displaying the kinds of characters I use in source code. This
# isn't particularly useful for scientific work, except maybe for helping
# people decide which languages use more sigils, and if a particular language
# may increase the risks of RSI.

#
import getopt
import os
import sys


# Dictionary to store all the characters and their respective counts.
_chardict = {}

# Counter to track the number of files analyzed.
_fnum = 0

# An incomplete list of accepted filenames. Files with other extensions (or
# without one) are not processed. Binary files using one of these extensions
# will be processed.
_exts = ['a', 'ada', 'adb', 'ads', 'applescript', 'as', 'ascx', 'asm', 'asmx',
    'asp', 'aspx', 'awk', 'bib', 'c', 'cc', 'clj', 'cobol', 'coffee', 'conf',
    'cpp', 'cs', 'csd', 'css', 'cxx', 'd', 'diff', 'dtd', 'e', 'erb', 'f',
    'f90', 'for', 'fpp', 'h', 'hs', 'htaccess', 'htm', 'html', 'java', 'js',
    'jsp', 'jsx', 'lhs', 'lisp', 'lsp', 'lua', 'm', 'markdown', 'md', 'mdown',
    'ml', 'mm', 'orc', 'php', 'pl', 'plis', 'pm', 'pro', 'prolog', 'py', 'r',
    'rb', 'rhtml', 's', 'scala', 'sco', 'scpt', 'sh', 'sql', 'tcl', 'tex',
    'text', 'textile', 'tk', 'txt', 'vb', 'xhtm', 'xhtml', 'xml', 'xsd',
    'xsl', 'xslt']

# The column widht to use for printing
COL_WIDTH = 10

# The error code for incorrect arguments (number or type of)
ERR_ARGS = 1
# The error code for invalid arguments (non-existent paths)
ERR_INVALID = 2
# Guru Meditation
ERR_GURU = 127

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
            for root, dirs, files in os.walk(fullpath):
                for fname in files:
                    count_file(os.path.join(root, fname))
        else:
            count_file(fullpath)

    print_stats()

# Print a helpful message to the user, informing of the various options the
# program understands.

def usage():
    sys.stdout.write('Usage:\n')
    sys.stdout.write('\t%s file_or_folder_1 <others ...>\n' % sys.argv[0])

# Verify that we should analyze this file (based on extension) and, if true, 
# update the character stats

def count_file(path):
    global _fnum
    path_ext = os.path.splitext(path)[1][1:]
    if path_ext and path_ext in _exts:
        _fnum += 1
        with open(path) as fd:
            for l in fd.readlines():
                for c in l:
                    v = _chardict.setdefault(c, 0)
                    _chardict[c] = v + 1

# Prepares and prints the various statistics. More to come.

def print_stats():
    total = 0
    alpha = 0
    digit = 0
    space = 0
    other = 0
    # Compute how many characters from each class have been encountered.
    for k in sorted(_chardict):
        addval = _chardict[k]
        if k.isalpha():
            alpha += addval
        elif k.isdigit():
            digit += addval
        elif k.isspace():
            space += addval
        else:
            other += addval
        total += _chardict[k]

    sys.stdout.write('\n')
    sys.stdout.write('files: %s\n' % str(_fnum).rjust(COL_WIDTH))
    sys.stdout.write('\n')
    sys.stdout.write('alpha: %s\n' % str(alpha).rjust(COL_WIDTH))
    sys.stdout.write('digit: %s\n' % str(digit).rjust(COL_WIDTH))
    sys.stdout.write('space: %s\n' % str(space).rjust(COL_WIDTH))
    sys.stdout.write('other: %s\n' % str(other).rjust(COL_WIDTH))
    sys.stdout.write(('=' * (7 + COL_WIDTH)) + '\n')
    sys.stdout.write('total: %s\n' % str(total).rjust(COL_WIDTH))

# Run the program.
if __name__ == '__main__':
    main(sys.argv[1:])
