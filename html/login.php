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
    if (isset($_POST['login'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        if (!empty($username) && !empty($password)) {
            $db = pg_connect('host=localhost dbname=cs160 user=postgres password=pass');

            $res = pg_prepare($db, '', 'SELECT user_id FROM users WHERE username = $1 AND password = $2;');
            $res = pg_execute($db, '', [$username, $password]);
            $arr = pg_fetch_all($res);

            if ($arr) {
                $_SESSION['user_id'] = $arr[0]['user_id'];
                header('location: home.php');
            } else {
                $error = 'Wrong username or password.';
            }
        } else {
            $error = 'Empty field(s).';
        }
    }
}
