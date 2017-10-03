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
import sys

import cv2
import psycopg2

IMAGE_DIR = '../src/image/'


def point_rect(point, rect):
    if point[0] < rect[0]:
        return False
    elif point[1] < rect[1]:
        return False
    elif point[0] > rect[2]:
        return False
    elif point[1] > rect[3]:
        return False
    return True


def draw_points(image, points, color=(0, 0, 255)):
    for p in points:
        cv2.circle(image, p, 3, color, cv2.FILLED, cv2.LINE_AA, 0)


def draw_delaunay(image, subdiv, color=(255, 0, 0)):
    rect = 0, 0, image.shape[1], image.shape[0]
    triangles = subdiv.getTriangleList()
    for t in triangles:
        p1 = t[0], t[1]
        p2 = t[2], t[3]
        p3 = t[4], t[5]
        if point_rect(p1, rect) and point_rect(p2, rect) and point_rect(p3, rect):
            cv2.line(image, p1, p2, color, 1, cv2.LINE_AA, 0)
            cv2.line(image, p2, p3, color, 1, cv2.LINE_AA, 0)
            cv2.line(image, p3, p1, color, 1, cv2.LINE_AA, 0)


def main(video_id):
    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    for image_file in os.listdir(IMAGE_DIR + video_id):
        frame_no = image_file.split('.')[0]

        image = cv2.imread(IMAGE_DIR + video_id + '/' + image_file)

        sql = '''SELECT * FROM landmark WHERE video_id = %s AND frame_no = %s;'''
        arg = video_id, frame_no
        cur.execute(sql, arg)

        landmarks, subdiv = [], cv2.Subdiv2D((0, 0, image.shape[1], image.shape[0]))

        for points in cur.fetchone()[2:]:
            x, y = points[1:-1].split(',')
            point = min(image.shape[1] - 1, int(round(float(x)))), min(image.shape[0] - 1, int(round(float(y))))
            landmarks.append(point)
            subdiv.insert(point)

        draw_points(image, landmarks)
        draw_delaunay(image, subdiv)

        sql = '''SELECT left_eye, right_eye FROM pupil WHERE video_id = %s AND frame_no = %s;'''
        arg = video_id, frame_no
        cur.execute(sql, arg)

        pupils = []

        for points in cur.fetchone():
            x, y = points[1:-1].split(',')
            point = min(image.shape[1] - 1, int(x)), min(image.shape[0] - 1, int(y))
            pupils.append(point)

        draw_points(image, pupils, (0, 255, 255))

        cv2.imwrite(IMAGE_DIR + video_id + '/' + frame_no + '_o.png', image)

    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print('Usage: process video_id')
        sys.exit(-1)
