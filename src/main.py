import numpy as np
import  RLE_coder as rle
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class RLE_api(Resource):
    def get(self, url):
        #Load image
        im = rle.get_image("https://picsum.photos/256/256")
        #Original size data
        n, m = im.shape
        im_bits = n * m
        bit_code_seq, size = rle.compress_image_RLE(im)
        return {'Uncomp_size': str(im_bits), 'Bit_Sequence': bit_code_seq, 'Comp_size': size}
    def post(self):
        return  {'data': 'Posted'}

api.add_resource(RLE_api, '/rle_encoder/<string:url>')

if __name__ == '__main__':
    app.run(debug=True)








