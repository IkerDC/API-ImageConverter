import requests
import cv2
import numpy as np

#URL
BASE = "http://127.0.0.1:7000/"

def conv_options():

    '''
    This function will read input form the user where the conversion format and extra operation is specified.

    :return: Format and operation
    '''
    print('Write the format to convert into from: [bmp, jpeg, png, webp]')
    form = input()
    print('Write extra operation to perform to the image:\n'
          '[none]: Any operation will be applied\n'
          '[bw]: Convert image to grayscale/Black and White\n'
          '[canny]: Image filtered with a canny filter to detect the edges\n'
          '[bin]: Binarize the image\n'
          '[rot180]: Rotate the image 180º\n')
    op = input()
    return form, op

def check_response(response,form):
    '''
    This function will take the response from the API and check whether the response is an image, an therefore it saves it,
    or if the response its an error message

    :param response: Response from the API
    :return:
    '''

    #If we are getting ascii encoding, it means that we have a string returned, not a file! Else, we have a file
    if(response.apparent_encoding == 'ascii'):
        return response.content
    else:
        nparr = np.frombuffer(response.content, np.uint8)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite('Conv_Im.'+form, img)
        return 'SUCCESS: Converted image saved (as Conv_Im.'+form+')'

def callAPI():
    '''
    Function to call the API. It is structured for the user to implement a menu to call more than once the API.
    :return: True is the call was right, False otherwise
    '''

    print('Introduce the image filename to convert:')
    filename = input()
    form, op = conv_options()

    #Check if the any of the inputs has any forward slash that could disrupt the endpoints
    if( 1 + (filename+form+op).find('/')):
        print("ERROR: The filename, format or operation introduced contains illegal characters")
        return  False
    else:
        endpoints = "image/" + filename + "/" + form + "/" + op
        response = requests.post(BASE + endpoints)

        #IT
        print(check_response(response, form))
        return True

resp = callAPI()