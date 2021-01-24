# API-ImageConverter :camera:
API to change image format + extra opertaions.


## The Project
This is my first API. I've done it in order to know a bit better how they wotkr, get used to the *get, post, ...* requestes. 
I have done it in Python using Flask. The API will take a given file (an image) in one of the supoorted formats, and will converted to the new desired format along with one of the other extra operations available.

### Functioning
The user provide a file name of the image to convert. The image provided must existis where the app is running. Once the image is read, along with the new format to conver and the extra operation (if one is selected), using OpenCV, a new temp file will be generted in the app path, then returned to the user using the *send_file* function from Flask. Once the user recives the image, it will be decoded and saved.

## Requirements
```
pip install -r requirements.txt
```

## Contact

Iker Diaz Cilleruelo - iker.diaz01@estudiant.upf.edu

Project Link: [https://github.com/IkerDC/SCAV-P2](https://github.com/IkerDC/SCAV-P2)
