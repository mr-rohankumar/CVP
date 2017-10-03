# CVP (SJSU CS 160, SPRING 2017)

![Icon](https://i.imgur.com/ougg2B7.png)

## Purpose:
CVP, or computer vision pipeline, is a web-based client to draw a face mesh for an uploaded video of user's choosing; Active Appearence Modelling algorithm from OpenFace to locate facial features and Delaunay Triangulation from OpenCV to create a face mesh.

![Sample](https://i.imgur.com/tdRB7kR.png)

## Implementation:  
* Frontend:
  * User login / User sign up
    * Sanitize user input
    * Authenticate user / Add user
      * Insert username, password, first_name, last_name, last_see, and ip_addr to database; and get user_id
  * User uploads video to upload directory
    * Sanitize video input (i.e., validate and rename)
      * ```<user_id>.<time_stamp>```
* Backend:
  * Get metadata from video
    * FFprobe
      * Get width, height, frame_rate, and frame_count
    * Insert user_id, width, height, frame_rate, and frame_count to database; and get video_id
    * Rename video and move to video directory
      * ```<video_id>```
  * Extract frames from video
    * FFmpeg (png)
      * Output to image directory
  * Analyse frames
    * OpenFace / EyeLike
      * Get landmark, pose, and pupil
    * Insert landmark, pose, and pupil to database
  * Process frames
    * Get landmark and pupil from database
    * OpenCV
      * Draw points and delaunay triangles
  * Create video from frames
    * Get frame_rate from database
    * FFmpeg (webm)
* Frontend:
  * Display video to user

![Design](https://i.imgur.com/6xuoi0W.png)

## Instructions: 
1. Clone repository / extract zip file to document root of web server.
2. Extract ```src/bin/FaceLandmarkImg.zip``` and ```src/bin/eyeLike.zip``` in place.
3. Run ```python cvp_init.py``` in ```src``` directory to initalize database tables.
4. Open ```http://localhost``` using a web browser of choosing.

## Limitations:
For demonstration purposes only, that is, not to be used in live production.

## Dependencies:
* Apache 2.4.25
* [eyeLike](https://github.com/trishume/eyeLike)
* FFmpeg 3.3
* OpenCV 3.3
* [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace)
* PHP 7.1.2 
* Postgresql 9.5.6
* Psycopg2 2.7.3
* Python 2.7.13

## License
```
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
```
