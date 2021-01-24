import cv2

formats = ['bmp','jpeg','png','webp']
operation =['none', 'bw','canny', 'bin','rot180']

def check_format(file_name):
    '''
    This function will check if the inout passed is correct. If it is indeed an image and its extension is one of
    the support for conversion.

    :param file_name: Name of the file where the extension appears
    :param formats: List of available formats
    :return: True/False if the format is supported
    '''
    #Find where the extension begins
    ext_start = file_name.rfind('.')
    ext = file_name[ext_start+1:]

    #Check if the format is supported
    if(ext in formats):
        return True
    else:
        return False

def check_conv_op(new_format, op):

    '''
    Function to check if the required conversion is available for the given format, as well as the operation.

    :param new_format: Format to convert into
    :param op: Operation to perform upon the image
    :return: True/False if the format conversion+operation if available
    '''

    if(new_format in formats):
        if(op in operation):
            return True
        else:
            return False
    else:
        return  False

def convert(im, op):

    '''
    The function will take an image and perform the required operation

    :param im: Image to convert
    :param op: Format to convert into
    :return: Converted image
    '''
    new_in = im
    #Operate
    if(op=='none'):
        new_in = im
    elif(op == 'bw'):
        new_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    elif(op == 'canny'):
        new_im = cv2.Canny(im,100,200)
    elif (op == 'bin'):
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, new_im = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    else:
        new_im = cv2.rotate(im, cv2.ROTATE_180)
    return new_im

