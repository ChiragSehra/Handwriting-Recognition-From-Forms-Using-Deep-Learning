import numpy as np
import cv2


def skewnessDetection(originalImage):
    """
    Returns the angle of the image that is being passed to check the skewness of the form image.

    """
    try:
        print("[INFO]: Width of Original Image: {0} and Height of Original Image: {1}".format(originalImage.shape[0], originalImage.shape[1]))
        gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)
        # plt.plot()
        # plt.imshow(gray)
        # cv2.imwrite("gray_bitnot.jpg",gray)

        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        coords = np.column_stack(np.where(thresh > 0))
        # print('Thresh: {}'.format(thresh))
        # print('Coordinates: {}'.format(coords))

        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        h, w = originalImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        #         print ("[INFO]: Rotation Matrix for the image is: {}".format(M))
        rotated = cv2.warpAffine(originalImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        # cv2.imwrite("temporaryResults/rotated.jpg",rotated)
        print("[INFO] Rotation angle: {}".format(angle))
        #         if angle < 0:
        #             raise Exception("Form is rotated. Please scan it again to proceed.")
        # if not -180.0 <= angle <= -179.0 or not 0.0 <= angle <= 0.05:
        #     print ("Form can be process further..")
        # else:
        #     print ("You have not scanned the form properly.\n Please scan it properly and ensure cropping is done "
        #            "correctly.")

        # if angle < 0:
        #     rotatingAngle = abs (angle) - 180
        # else:
        #     rotatingAngle = -angle
        # # rotatedImage = rotate (originalImage, rotatingAngle, reshape = False)
        #
        # rotatedImage = rotate(originalImage,-1.07,reshape = False)
        # cv2.imwrite ("temporaryResults/rotated.jpg", rotated)
        # # cv2.imwrite("../temporaryResults/newImg-.jpg", rotatedImage)

        print("[PROCESS COMPLETION]: Skewness Detection Completed..")
        return angle
    except AttributeError as e:
        raise Exception("Image not found at specified path.")

# form_image = url_to_image(image_url=url)
# originalImage = cv2.imread("/home/srijan/Downloads/githubUpload/buddy-module/formImages/front/new/sachin_front.jpg")
# skewnessDetection(originalImage = originalImage)
