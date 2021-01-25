# API-ImageConverter :camera:
API to change image format + extra operations.


## The Project
This is my first API. I've done it in order to know a bit better how they work, get used to the *get, post, ...* requestes. \
I have done it in Python using Flask. The API will take a given file (an image) in one of the supported formats, and will converted to the new desired format along with one of the other extra operations available.

### Functioning
The user provides the file name of the image to convert. The image provided must exist where the app is running. Once the image is read, along with the new format to conver and the extra operation (if one is selected), using OpenCV, a new temp file will be generted in the app path, then returned to the user using the *send_file* function from Flask. Once the user recives the image, it will be decoded and saved.

## Requirements
```
pip install -r requirements.txt
```

## Opertaions
The following are the formarts to convert to/from, and the extra opertaion are:\
* **Formats**: 
  * *.png, .jpeg, .bmp, .webp*
* **Operations**:
  * *None*: Any other operation will be perfomed.
  * *BW*: Turn the image into gray scale.
  * *Canny*: Filter the image with a canny filter to obtain the edges.
  * *Bin*: Binarize the image.
  * *rot180*: Rotate the image 180º.
## Contact

Iker Diaz Cilleruelo - ikerdiaz1312@gmail.com

Project Link: [https://github.com/IkerDC/SCAV-P2](https://github.com/IkerDC/SCAV-P2)
