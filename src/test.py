import requests
import RLE_coder as rle
import matplotlib.pyplot as plt

BASE = "http://127.0.0.1:5000/"

url = "55/8"
response = requests.get(BASE + "rle_encoder/"+url)
data = response.json()
print("Original data:",data["Uncomp_size"],"bits")
print("Compressed data:",data["Comp_size"],"bits")
print("Show compressed image bit sequence? ([0]:No, [1]:Yes)")
show = input()
if (show == 1):
    print(data["Bit_Sequence"])
print("Do you want to reconstruct the image? ([0]:No, [1]:Yes)")
rec = input()
if (rec == 1):
    recov_image = rle.decode_image_RLE(data["Bit_Sequence"])
    f = plt.figure()
    plt.imshow(recov_image,cmap='Greys')
    plt.show(block=True)