#!/usr/bin/env python

import os.path as path
from shutil import copyfile
from glob import glob

LINE_CSS_STRUCT = "%s/Contents/Resources/skin/mac/css/"


def update_line_css(source, line_app_path):
    "Update Line's CSS from source"
    line_css_path = LINE_CSS_STRUCT % (line_app_path)

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
            return 0


def main():
    source = "./"
    line_app = "/Applications/Line.app"

    update_line_css(source, line_app)

if __name__ == "__main__":
    main()
