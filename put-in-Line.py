#!/usr/bin/env python

import os.path as path
from shutil import copyfile
from shutil import move
from glob import glob

LINE_CSS_STRUCT = "%s/Contents/Resources/skin/mac/css/"


def update_line_css(source, line_app_path):
    "Update Line's CSS from source"
    line_css_path = LINE_CSS_STRUCT % (line_app_path)

    if path.exists(line_css_path) is False:
        return

    for filename in glob("%s*.css" % (source)):
        a_css_path = line_css_path + filename

        if __debug__:
            print "from: %s to %s" % (filename, line_css_path)

        # has old css, backup it
        if path.exists(a_css_path):

            css_backup_path = line_css_path + filename + ".backup"

            if __debug__:
                print "backup old file: %s" % (css_backup_path)

            move(a_css_path, css_backup_path)

        try:
            copyfile(filename, a_css_path)
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
