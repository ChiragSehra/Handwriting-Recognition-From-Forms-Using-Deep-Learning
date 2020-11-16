# importing libraries
import numpy as np
import cv2


def preprocess(img_grey):
    #     [RUBBERDUCK] = [Change the path to S3 url where these temporary images will be stored.]
    """
    Function to preprocess the image for image segmentation.
    Arguments:
        img_grey: GrayScale format of the image to be pre - processed.
    """
    (thresh, img) = cv2.threshold(img_grey, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)

    img = cv2.bitwise_not(img)
    cv2.imwrite('temporaryResults/bitwiseNot.jpg', img)

    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    horizontal = th2
    rows, cols = horizontal.shape
    horizontalsize = int(cols / 45)
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
    horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
    horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))
    cv2.imwrite("temporaryResults/horizontal.jpg", horizontal)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # inverse the image, so that lines are black for masking
    horizontal_inv = cv2.bitwise_not(horizontal)
    # perform bitwise_and to mask the lines with provided mask
    masked_img = cv2.bitwise_and(img, img, mask=horizontal_inv)
    # reverse the image back to normal
    masked_img_inv = cv2.bitwise_not(masked_img)
    cv2.imwrite("temporaryResults/temp1.jpg", masked_img_inv)

    # Vertical line removal
    img2 = cv2.imread("temporaryResults/temp1.jpg")
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img2 = cv2.bitwise_not(img2)
    th3 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    vertical = th3
    verticalsize = int(rows / 70)
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
    vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
    vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))
    cv2.imwrite("temporaryResults/vertical.jpg", vertical)

    vertical_inv = cv2.bitwise_not(vertical)
    # perform bitwise_and to mask the lines with provided mask
    masked_img2 = cv2.bitwise_and(img2, img2, mask=vertical_inv)
    # reverse the image back to normal
    masked_img_inv2 = cv2.bitwise_not(masked_img2)
    # cv2.imshow("vertical_bitwise_not", vertical)
    cv2.imwrite("temporaryResults/temp2.jpg", masked_img_inv2)

    # Remove spots from the final output
    image = cv2.imread('temporaryResults/temp2.jpg')
    # Denoising spots
    # image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,30)
    img_bw = 255 * (cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')
    se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    img_mask = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, se1)
    img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, se2)

    img_mask = np.dstack([img_mask, img_mask, img_mask]) / 255
    output = image * img_mask
    cv2.imwrite('temporaryResults/output.png', output)
    print("[PROCESS COMPLETION]: Preprocessing Completed..!")
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
