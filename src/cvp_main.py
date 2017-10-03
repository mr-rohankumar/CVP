#!/usr/bin/python

"""
MIT License

Copyright (c) 2017 Rohan Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import division, print_function

import subprocess
import sys
from datetime import datetime

PYTHON_PATH = '/usr/bin/python'


def main(video_file):
    print('--------------------------------')
    print('|      STAGE #1: Metadata      |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/metadata.py', video_file]
    video_id, width, height, frame_rate, frame_count = subprocess.check_output(cmd, universal_newlines=True).split(',')
    print('video_id     =  ' + video_id)
    print('width        =  ' + width)
    print('height       =  ' + height)
    print('frame_rate   =  ' + str(eval(frame_rate)))
    print('frame_count  =  ' + frame_count.strip())
    print(str(datetime.now()) + '\t...done!\n')

    print('--------------------------------')
    print('|      STAGE #2: Extract       |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/extract.py', video_id]
    subprocess.check_call(cmd)
    print(str(datetime.now()) + '\t...done!\n')

    print('--------------------------------')
    print('|      STAGE #3: Analyse (1/2) |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/analyse_1.py', video_id]
    subprocess.check_call(cmd)
    print(str(datetime.now()) + '\t...done!\n')

    print('--------------------------------')
    print('|      STAGE #4: Analyse (2/2) |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/analyse_2.py', video_id]
    subprocess.check_call(cmd)
    print(str(datetime.now()) + '\t...done!\n')

    print('--------------------------------')
    print('|      STAGE #5: Process       |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/process.py', video_id]
    subprocess.check_call(cmd)
    print(str(datetime.now()) + '\t...done!\n')

    print('--------------------------------')
    print('|      STAGE #6: Create        |')
    print('--------------------------------')
    cmd = [PYTHON_PATH, '../src/create.py', video_id]
    subprocess.check_call(cmd)
    print(str(datetime.now()) + '\t...done!\n')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: cvp_main video_file')
        sys.exit(-1)
