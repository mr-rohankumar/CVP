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

$error = '';

if (isset($_SESSION['user_id'])) {
    header('location: home.php');
} else {
    if (isset($_POST['register'])) {
        $first_name = trim($_POST['first_name']);
        $last_name = trim($_POST['last_name']);
        $username = trim($_POST['username']);
        $password_1 = trim($_POST['password_1']);
        $password_2 = trim($_POST['password_2']);

        if (!empty($first_name) && !empty($last_name) && !empty($username) && !empty($password_1) && !empty($password_2)) {
            if ($password_1 == $password_2) {
                $db = pg_connect('host=localhost dbname=cs160 user=postgres password=pass');

                $res = pg_prepare($db, '', 'SELECT user_id FROM users WHERE username = $1;');
                $res = pg_execute($db, '', [$_POST['username']]);
                $arr = pg_fetch_all($res);

                if ($arr) {
                    $error = 'Duplicate username.';
                } else {
                    $res = pg_prepare($db, '', 'INSERT INTO users (first_name, last_name, username, password, last_seen, ip_addr) VALUES ($1, $2, $3, $4, NOW(), $5) RETURNING user_id;');
                    $res = pg_execute($db, '', [$first_name, $last_name, $username, $password_1, $_SERVER['REMOTE_ADDR']]);
                    $arr = pg_fetch_all($res);

                    $_SESSION['user_id'] = $arr[0]['user_id'];
                    header('location: home.php');
                }
            } else {
                $error = 'Mismatch password.';
            }
        } else {
            $error = 'Empty field(s).';
        }
    }
}
