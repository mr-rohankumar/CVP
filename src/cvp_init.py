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

import sys

import psycopg2


def main():
    con = psycopg2.connect(host='localhost', dbname='cs160', user='postgres', password='pass')
    cur = con.cursor()

    cur.execute('''CREATE TABLE users     (
                                               user_id         SERIAL      PRIMARY KEY,
                                               first_name      TEXT        NOT NULL,
                                               last_name       TEXT        NOT NULL,
                                               username        TEXT        NOT NULL,
                                               password        TEXT        NOT NULL,
                                               last_seen       TIMESTAMP   NOT NULL,
                                               ip_addr         TEXT        NOT NULL
                                         );
                ''')

    cur.execute('''CREATE TABLE video    (
                                               video_id        SERIAL      PRIMARY KEY,
                                               user_id         INTEGER     REFERENCES users(user_id),
                                               width           INTEGER     NOT NULL,
                                               height          INTEGER     NOT NULL,
                                               frame_rate      TEXT        NOT NULL,
                                               frame_count     INTEGER     NOT NULL
                                         );
                ''')

    cur.execute('''CREATE TABLE landmark (
                                               video_id        INTEGER     REFERENCES video(video_id),
                                               frame_no        INTEGER     NOT NULL,
                                               point_0         POINT       NOT NULL,
                                               point_1         POINT       NOT NULL,
                                               point_2         POINT       NOT NULL,
                                               point_3         POINT       NOT NULL,
                                               point_4         POINT       NOT NULL,
                                               point_5         POINT       NOT NULL,
                                               point_6         POINT       NOT NULL,
                                               point_7         POINT       NOT NULL,
                                               point_8         POINT       NOT NULL,
                                               point_9         POINT       NOT NULL,
                                               point_10        POINT       NOT NULL,
                                               point_11        POINT       NOT NULL,
                                               point_12        POINT       NOT NULL,
                                               point_13        POINT       NOT NULL,
                                               point_14        POINT       NOT NULL,
                                               point_15        POINT       NOT NULL,
                                               point_16        POINT       NOT NULL,
                                               point_17        POINT       NOT NULL,
                                               point_18        POINT       NOT NULL,
                                               point_19        POINT       NOT NULL,
                                               point_20        POINT       NOT NULL,
                                               point_21        POINT       NOT NULL,
                                               point_22        POINT       NOT NULL,
                                               point_23        POINT       NOT NULL,
                                               point_24        POINT       NOT NULL,
                                               point_25        POINT       NOT NULL,
                                               point_26        POINT       NOT NULL,
                                               point_27        POINT       NOT NULL,
                                               point_28        POINT       NOT NULL,
                                               point_29        POINT       NOT NULL,
                                               point_30        POINT       NOT NULL,
                                               point_31        POINT       NOT NULL,
                                               point_32        POINT       NOT NULL,
                                               point_33        POINT       NOT NULL,
                                               point_34        POINT       NOT NULL,
                                               point_35        POINT       NOT NULL,
                                               point_36        POINT       NOT NULL,
                                               point_37        POINT       NOT NULL,
                                               point_38        POINT       NOT NULL,
                                               point_39        POINT       NOT NULL,
                                               point_40        POINT       NOT NULL,
                                               point_41        POINT       NOT NULL,
                                               point_42        POINT       NOT NULL,
                                               point_43        POINT       NOT NULL,
                                               point_44        POINT       NOT NULL,
                                               point_45        POINT       NOT NULL,
                                               point_46        POINT       NOT NULL,
                                               point_47        POINT       NOT NULL,
                                               point_48        POINT       NOT NULL,
                                               point_49        POINT       NOT NULL,
                                               point_50        POINT       NOT NULL,
                                               point_51        POINT       NOT NULL,
                                               point_52        POINT       NOT NULL,
                                               point_53        POINT       NOT NULL,
                                               point_54        POINT       NOT NULL,
                                               point_55        POINT       NOT NULL,
                                               point_56        POINT       NOT NULL,
                                               point_57        POINT       NOT NULL,
                                               point_58        POINT       NOT NULL,
                                               point_59        POINT       NOT NULL,
                                               point_60        POINT       NOT NULL,
                                               point_61        POINT       NOT NULL,
                                               point_62        POINT       NOT NULL,
                                               point_63        POINT       NOT NULL,
                                               point_64        POINT       NOT NULL,
                                               point_65        POINT       NOT NULL,
                                               point_66        POINT       NOT NULL,
                                               point_67        POINT       NOT NULL
                                         );
                ''')

    cur.execute('''CREATE TABLE head     (
                                               video_id        INTEGER     REFERENCES video(video_id),
                                               frame_no        INTEGER     NOT NULL,
                                               pitch           REAL        NOT NULL,
                                               yaw             REAL        NOT NULL,
                                               roll            REAL        NOT NULL
                                         );
                ''')

    cur.execute('''CREATE TABLE pupil    (
                                               video_id        INTEGER     REFERENCES video(video_id),
                                               frame_no        INTEGER     NOT NULL,
                                               left_eye        POINT       NOT NULL,
                                               right_eye       POINT       NOT NULL
                                         );
                ''')

    con.commit()
    cur.close()
    con.close()


if __name__ == "__main__":
    main()
    sys.exit(0)
