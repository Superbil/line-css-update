#!/usr/bin/env python

import os.path as path
from shutil import copyfile
from glob import glob

LINE_CSS_STRUCT = "%s/Contents/Resources/skin/mac/css/"


def update_line_css(source, line_path):
    "Update Line's CSS from source"
    line_css_path = LINE_CSS_STRUCT % (line_path)

    if path.exists(line_css_path) is False:
        return

    for filename in glob("%s*.css" % (source)):
        if __debug__:
            print "from: %s to %s" % (filename, line_css_path)

        try:
            copyfile(filename, line_css_path + filename)
        except IOError as e:
            if __debug__:
                print e
            break


def main():
    source = "./"
    line = "/Applications/Line.app"

    update_line_css(source, line)

if __name__ == "__main__":
    main()
