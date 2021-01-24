from flask import Flask, send_file
import image_conv as conv
import cv2
import os


app = Flask(__name__)

@app.route('/image/<string:filename>/<string:format>/<string:op>', methods = ['POST'])
def convert(filename, format, op):

    if not os.path.exists(filename):
        return 'The specified file does not exist'
    else:
        #Check that all the inputs are correct, if so, to the conversion and operate
        if(conv.check_format(filename)):
            if(conv.check_conv_op(format,op)):

                #Read the data with the image and decode it
                img = cv2.imread(filename)

                #Perform the operation and save image to new format
                img = conv.convert(img,op)

                #Read the name of the file without the extension
                name = filename[:filename.rfind('.')+1]

                #Write the image and return it. We have to store it in memory so the image can be deleted
                cv2.imwrite('temp_' + name + format, img)


                return send_file('temp_' + name + format, mimetype='image/' + format, as_attachment='conv_' + name + format)

            else:
                return 'ERROR: The specified format to convert into, or the operation specified are not available.'

        else:
            return 'ERROR: The file extension provided is not supported. Please provide a supported file.'



if __name__ == '__main__':
    app.run(debug=True, port=7000)











