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
include('register.php')
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up | CVP</title>
    <link href="css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
<div class="container" id="center-justify">
    <h1>Sign Up</h1>

    <form method="post">
        <input name="first_name" placeholder="First Name" type="text">
        <input name="last_name" placeholder="Last Name" type="text">
        <input name="username" placeholder="Username" type="text">
        <input name="password_1" placeholder="Choose Password" type="password">
        <input name="password_2" placeholder="Verify Password" type="password">
        <span><?= $error ?></span>
        <input name="register" value="Register" type="submit">
    </form>

    <form action="index.php">
        <button>Cancel</button>
    </form>
</div>
</body>
</html>
