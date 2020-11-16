## Importing libraries
import numpy as np
import urllib.request
import cv2


# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(image_url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(image_url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print("Width and Height of Original Image are :  {0} and {1}".format(image.shape[1],image.shape[0]))
    return image

# s3_url = ""
# image = url_to_image(image_url=s3_url)
