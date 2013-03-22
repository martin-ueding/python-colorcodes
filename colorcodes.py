#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                License (MIT)                                #
###############################################################################
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import subprocess

__docformat__ = "restructuredtext en"

class Colorcodes(object):
    """
    Provides ANSI terminal color codes which are gathered via the ``tput``
    utility. That way, they are portable. If there occurs any error with
    ``tput``, all codes are initialized as an empty string.

    The provided fields (plain strings, i. e. unicode) are listed below.

    Control:

    - bold
    - reset

    Colors:

    - blue
    - green
    - orange
    - red

    :license: MIT
    """
    def __init__(self):
        try:
            self.bold = subprocess.check_output("tput bold".split()).decode()
            self.reset = subprocess.check_output("tput sgr0".split()).decode()

            self.red = subprocess.check_output("tput setaf 1".split()).decode()
            self.green = subprocess.check_output("tput setaf 2".split()).decode()
            self.orange = subprocess.check_output("tput setaf 3".split()).decode()
            self.blue = subprocess.check_output("tput setaf 4".split()).decode()
            self.purple = subprocess.check_output("tput setaf 5".split()).decode()
            self.cyan = subprocess.check_output("tput setaf 6".split()).decode()
            self.white = subprocess.check_output("tput setaf 7".split()).decode()
        except subprocess.CalledProcessError as e:
            self.bold = ""
            self.reset = ""

            self.blue = ""
            self.green = ""
            self.orange = ""
            self.red = ""
            self.cyan = ""
            self.purple = ""
            self.white = ""
