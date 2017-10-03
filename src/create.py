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

import psycopg2

IMAGE_DIR = '../src/image/'
OUTPUT_DIR = './output/'


def main(video_id):
    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    sql = '''SELECT frame_rate FROM video WHERE video_id = %s;'''

    arg = video_id

    cur.execute(sql, arg)

    frame_rate = cur.fetchone()[0]

    con.commit()
    cur.close()
    con.close()

    cmd = ['/usr/bin/ffmpeg', '-v', 'quiet', '-r', frame_rate, '-i', IMAGE_DIR + video_id + '/%d_o.png',
           '-c:v', 'libvpx-vp9', '-b:v', '1M', OUTPUT_DIR + video_id + '.webm']

    subprocess.check_call(cmd)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: create video_id')
        sys.exit(-1)
