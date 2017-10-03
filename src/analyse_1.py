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

FEATURE_DIR = '../src/feature/'
IMAGE_DIR = '../src/image/'


def main(video_id):
    try:
        os.makedirs(FEATURE_DIR + video_id, 0o777)
    except OSError:
        pass

    cmd = ['../src/bin/FaceLandmarkImg', '-q', '-fdir', IMAGE_DIR + video_id,
           '-ofdir', FEATURE_DIR + video_id, '-wild', '-multi-view', '0']

    subprocess.check_call(cmd)

    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    for pts_file in os.listdir(FEATURE_DIR + video_id):
        frame_no = pts_file.split('_')[0]

        points, pose = [], []

        with open(FEATURE_DIR + video_id + '/' + frame_no + '_det_0.pts') as in_file:
            for line in in_file:
                if line == '{\n':
                    break

            for line in in_file:
                if line == '}\n':
                    break
                x, y = line.split(' ')
                point = str((float(x), float(y)))
                points.append(point)

            for line in in_file:
                if line == '{\n':
                    break

            for line in in_file:
                if line == '}\n':
                    break
                pose = line.split(' ')

        sql = '''INSERT INTO landmark (video_id, frame_no, point_0, point_1, point_2, point_3, point_4,
                                                           point_5, point_6, point_7, point_8, point_9,
                                                           point_10, point_11, point_12, point_13, point_14,
                                                           point_15, point_16, point_17, point_18, point_19,
                                                           point_20, point_21, point_22, point_23, point_24,
                                                           point_25, point_26, point_27, point_28, point_29,
                                                           point_30, point_31, point_32, point_33, point_34,
                                                           point_35, point_36, point_37, point_38, point_39,
                                                           point_40, point_41, point_42, point_43, point_44,
                                                           point_45, point_46, point_47, point_48, point_49,
                                                           point_50, point_51, point_52, point_53, point_54,
                                                           point_55, point_56, point_57, point_58, point_59,
                                                           point_60, point_61, point_62, point_63, point_64,
                                                           point_65, point_66, point_67)
                               VALUES (%s, %s, %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s,
                                               %s, %s, %s);'''

        arg = video_id, frame_no, points[0], points[1], points[2], points[3], points[4], \
              points[5], points[6], points[7], points[8], points[9], \
              points[10], points[11], points[12], points[13], points[14], \
              points[15], points[16], points[17], points[18], points[19], \
              points[20], points[21], points[22], points[23], points[24], \
              points[25], points[26], points[27], points[28], points[29], \
              points[30], points[31], points[32], points[33], points[34], \
              points[35], points[36], points[37], points[38], points[39], \
              points[40], points[41], points[42], points[43], points[44], \
              points[45], points[46], points[47], points[48], points[49], \
              points[50], points[51], points[52], points[53], points[54], \
              points[55], points[56], points[57], points[58], points[59], \
              points[60], points[61], points[62], points[63], points[64], \
              points[65], points[66], points[67]

        cur.execute(sql, arg)

        sql = '''INSERT INTO head (video_id, frame_no, pitch, yaw, roll) VALUES (%s, %s, %s, %s, %s);'''

        arg = video_id, frame_no, pose[0], pose[1], pose[2]

        cur.execute(sql, arg)

    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: analyse_1 video_id')
        sys.exit(-1)
