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

if (!isset($_SESSION['user_id'])) {
    header('location: index.php');
} else {
    if (isset($_POST['upload'])) {
        if ($_FILES['video']['error'] == UPLOAD_ERR_OK) {
            if (substr($_FILES['video']['type'], 0, 5) == 'video') {
                $video_file = $_SESSION['user_id'] . "." . time();

                move_uploaded_file($_FILES['video']['tmp_name'], './upload/' . $video_file);

                exec('/usr/bin/python' . ' ../src/cvp_main.py ' . $video_file . ' >> log.txt');

                header('location: home.php');
            } else {
                $error = 'File type not supported.';
            }
        } else {
            if ($_FILES['video']['error'] == UPLOAD_ERR_INI_SIZE || $_FILES['video']['error'] == UPLOAD_ERR_FORM_SIZE) {
                $error = 'File exceeds max file size.';
            } elseif ($_FILES['video']['error'] == UPLOAD_ERR_PARTIAL) {
                $error = 'Upload interrupted.';
            } elseif ($_FILES['video']['error'] == UPLOAD_ERR_NO_FILE) {
                $error = 'No file selected.';
            } else {
                $error = 'Upload error (' . $_FILES['video']['error'] . ').';
            }
        }
    }
}
