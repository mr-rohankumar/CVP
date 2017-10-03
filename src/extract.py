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

import os
import subprocess
import sys

IMAGE_DIR = '../src/image/'
VIDEO_DIR = '../src/video/'


def main(video_id):
    try:
        os.makedirs(IMAGE_DIR + video_id, 0o777)
    except OSError:
        pass

    cmd = ['/usr/bin/ffmpeg', '-v', 'quiet', '-i', VIDEO_DIR + video_id, IMAGE_DIR + video_id + '/%d.png']

    subprocess.check_call(cmd)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: extract video_id')
        sys.exit(-1)
