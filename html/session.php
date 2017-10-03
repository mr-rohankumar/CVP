/*
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
 */

<?php
session_start();

$name = '';
$file = [];

if (!isset($_SESSION['user_id'])) {
    header('location: index.php');
} else {
    $db = pg_connect('host=localhost dbname=cs160 user=postgres password=pass');

    $res = pg_prepare($db, '', 'UPDATE users SET last_seen = NOW(), ip_addr = $1 WHERE user_id = $2;');
    $res = pg_execute($db, '', [$_SERVER['REMOTE_ADDR'], $_SESSION['user_id']]);

    $res = pg_prepare($db, '', 'SELECT first_name FROM users WHERE user_id = $1;');
    $res = pg_execute($db, '', [$_SESSION['user_id']]);
    $arr = pg_fetch_all($res);

    $name = $arr[0]['first_name'];

    $res = pg_prepare($db, '', 'SELECT video_id FROM video WHERE user_id = $1;');
    $res = pg_execute($db, '', [$_SESSION['user_id']]);
    $arr = pg_fetch_all($res);

    foreach ($arr as $val) {
        $file[] = $val['video_id'];
    }
}
