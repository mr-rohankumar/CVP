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

UPSCALE_FACTOR = 0.02

IMAGE_DIR = '../src/image/'


def get_point(points, p, i):
    return float(points[p - 36][1:-1].split(',')[i])


def main(video_id):
    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    for image_file in os.listdir(IMAGE_DIR + video_id):
        frame_no = image_file.split('.')[0]

        sql = '''SELECT point_36, point_37, point_38, point_39, point_40, point_41,
                        point_42, point_43, point_44, point_45, point_46, point_47
                 FROM landmark WHERE video_id = %s AND frame_no = %s;'''

        arg = video_id, frame_no

        cur.execute(sql, arg)

        points = cur.fetchone()

        left_region_x = int(round(get_point(points, 36, 0) * (1 - UPSCALE_FACTOR)))

        left_region_y = int(round(min(get_point(points, 37, 1), get_point(points, 38, 1)) * (1 - UPSCALE_FACTOR)))

        left_region_width = int(round(get_point(points, 39, 0) * (1 + UPSCALE_FACTOR))) - left_region_x

        left_region_height = int(round(max(get_point(points, 40, 1), get_point(points, 41, 1))
                                       * (1 + UPSCALE_FACTOR))) - left_region_y

        right_region_x = int(round(get_point(points, 42, 0) * (1 - UPSCALE_FACTOR)))

        right_region_y = int(round(min(get_point(points, 43, 1), get_point(points, 44, 1)) * (1 - UPSCALE_FACTOR)))

        right_region_width = int(round(get_point(points, 45, 0) * (1 + UPSCALE_FACTOR))) - right_region_x

        right_region_height = int(round(max(get_point(points, 46, 1), get_point(points, 47, 1))
                                        * (1 + UPSCALE_FACTOR))) - right_region_y

        cmd = ['../src/bin/eyeLike', IMAGE_DIR + video_id + '/' + image_file,
               str(left_region_x), str(left_region_y), str(left_region_width), str(left_region_height),
               str(right_region_x), str(right_region_y), str(right_region_width), str(right_region_height)]

        left_eye_x, left_eye_y, right_eye_x, right_eye_y = subprocess.check_output(cmd,
                                                                                   universal_newlines=True).split(',')

        left_eye, right_eye = str((int(left_eye_x), int(left_eye_y))), str((int(right_eye_x), int(right_eye_y)))

        sql = '''INSERT INTO pupil (video_id, frame_no, left_eye, right_eye) VALUES (%s, %s, %s, %s);'''

        arg = video_id, frame_no, left_eye, right_eye

        cur.execute(sql, arg)

    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: analyse_2 video_id')
        sys.exit(-1)
