import numpy as np
import requests
import shutil
import matplotlib.pyplot as plt


def RLE(code, ref_character):

    '''
    This function will provide run length encoding following the definition of
    0 or 1 as reference and starting the counting depending on that value, so if the reference is 0
    and there is none 0's at the start, the length of the first count is 0.

    WORKS: We have a state, 0 or 1, in which we are, if the number is the same, we keep adding +1 and
    increasing the length, if the bit reed changes for the so called "state", so from 0 to 1 or from 1 to 0
    we do a new append and start counting how many of those bits follow!
    +Plus the code works with bits, characters, etc, etc, etc... Only for two values obviusly

    :param code: sequence of bits to code
    :param ref_character: reference bit to code
    :return: coded sequence
    '''

    encoded = []
    state = ref_character
    encoded.append(0)
    for i in code:
        if(state != i): #Check if the reed value is the actual
            encoded.append(0) #New "count"
            state = i #Update the sate
        encoded[-1] += 1 #-1 is the last position (and add 1)
    return np.array(encoded)

def inv_RLE(code, ref_character):

    '''
    This function will decode RLE encoding based the function to encode.

    :param code: coded sequence to decode
    :param ref_character: reference bit
    :return: decoded sequence
    '''
    decoded = []
    state = ref_character
    for i in code:
        for j in range(int(i)):
            decoded.append(state)
        # Change the state to now adding 0 or 1
        state = (int(state) + 1) % 2
    return decoded

def compress_image_RLE(im):

    '''
    This function will take a b/w image and codified using RLE. the way it will be done, is to use some metadata to codify
    every image line with different number of bits by number (i.e bit depth) because if we have an image with dimensions
    1280x720, and one line is all white, the RLE will value 1280, thus we need 11 bits to represent that number, but
    if the another line has more variability numbers will be smaller and we will need less bits. Therefore we will send
    first some metadata codifying this.
    The structure will be as follows:
    1. Send dimension of image (max size 4095 i.e will always be represented with 12 bits)
    2. For each line, metadata of bits used to encode that line
    3. RLE encoding

    :param im: Image (numpy matrix)
    :return: Bit sequence with metadata and image codified
    '''
    #dimensions
    n, m = im.shape
    #higher number of bits that can be need in each line. Metadata number of used bits per line (will be to represent n)
    line_bits = int(np.floor(np.log2(n))+1)
    bit_seq_coded_image = []
    #Begin by appending the image size (always use 12 bits)
    bit_seq_coded_image.append(bin(n)[2:].zfill(12))
    bit_seq_coded_image.append(bin(m)[2:].zfill(12))
    size = 0
    for i in range(n):
        code = RLE(im[i,:].tolist(),0)
        #Bits used to code the line
        n_bits = int(np.floor(np.log2(max(code)))+1)
        bit_seq_coded_image.append(bin(n_bits)[2:].zfill(line_bits))
        #Get the size of data we are generating
        size = size + (len(code)*n_bits)+line_bits
        for j in code:
            #Add each length from RLE to the sequence of to bits
            bit_seq_coded_image.append(bin(j)[2:].zfill(n_bits))

    return bit_seq_coded_image, size

def decode_image_RLE(bit_sequence):

    '''
    This function will decode the sequence of bits with the coded image using RLE and the metadata.
    It will first read the dimensions, and based on that obtain the rest of parameters needed to read the
    metadata and the based on those, read the compressed data

    :param bit_sequence: sequence of bits where the image is codified
    :return: image
    '''

    #dimensions. get the sequence to a unique string, and a string to int
    n = int(''.join(map(str, bit_sequence[0])),2)
    m = int(''.join(map(str, bit_sequence[1])), 2)
    #number of bits used in the metadata to code how many bits are used in a line
    line_bits = np.floor(np.log2(n))+1
    #Use a location pointer to know when we reach the end of a line and jump to the next one (we start first meta-dada bit)
    location = 2
    image = np.zeros((n,m))

    for i in range(n):
        #Bits to be counted by line (max will be the number of columns)
        bits_count = 0
        #Bits used to code the line values
        bit_steps = int(''.join(map(str, bit_sequence[location])), 2)
        #We have already read the number of bits used, so we jump them and start reading
        location = location+1
        code = []
        while(bits_count < m):
            #we read all the values from a line to decode it afterwards
            seq = int(''.join(map(str, bit_sequence[location])), 2)
            code.append(seq)
            #Update: number of bits counted (we count till the end of the line) and location on the string
            bits_count = bits_count+seq
            location = location+1
        #store the decoded line
        image[i,:]=inv_RLE(code,0)
    return image


def get_image(url):
    '''
    This function will take a PNG image from the internet, load it, and the it will converted to b/w and
    binarize it to then being encoded.

    :param url: URL where the image is stored
    :return: image
    '''

    #Load image
    response = requests.get(url, stream=True)
    with open('image.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    image = plt.imread('image.png', 'PNG')
    #to gray scale and normalize
    image = np.mean(image,2)/255
    #binarize image
    image = np.round(image)
    return image

