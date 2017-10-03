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

import psycopg2

UPLOAD_DIR = './upload/'
VIDEO_DIR = '../src/video/'


def main(video_file):
    user_id = video_file.split('.')[0]

    cmd = ['/usr/bin/ffprobe', '-v', 'quiet', '-count_frames', '-select_streams', 'v:0', '-show_entries',
           'stream=height,width,avg_frame_rate,nb_read_frames', '-of', 'csv=p=0:nk=1', UPLOAD_DIR + video_file]

    width, height, frame_rate, frame_count = subprocess.check_output(cmd, universal_newlines=True).split(',')

    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    sql = '''INSERT INTO video (user_id, width, height, frame_rate, frame_count)
             VALUES (%s, %s, %s, %s, %s) RETURNING video_id;'''

    arg = user_id, width, height, frame_rate, frame_count

    cur.execute(sql, arg)

    video_id = str(cur.fetchone()[0])

    con.commit()
    cur.close()
    con.close()

    os.rename(UPLOAD_DIR + video_file, VIDEO_DIR + video_id)

    print(video_id + ',' + width + ',' + height + ',' + frame_rate + ',' + frame_count)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: metadata video_file')
        sys.exit(-1)
