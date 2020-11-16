import cv2
from pprint import pprint
from helpers.modules.skewnessCorrection_02 import skewnessDetection
from helpers.modules.imageCropper_03 import imageCropping
from helpers.modules.templateMatching_04 import templateMatcher
from helpers.modules.preprocessing_05 import preprocess
from helpers.modules.imageSegmentation_06 import imageSegmentation
from helpers.modules.checkboxDetection_07 import checkboxDetection
from helpers.modules.imageStitching_08 import imageStitching
from helpers.modules.documentDetection_09 import documentDetection

pathToFile = "../formImages/front/Bandana_front.jpg"


def main(form_side, user_id):
    # returns image from s3 url
    image = cv2.imread(pathToFile)
    lettersAndDigits = string.ascii_letters + string.digits
    final_userId = ''.join(random.choice(lettersAndDigits) for i in range(6))
    user_id = final_userId
    # check for skewness and save a rotated image into temporaryResults folder
    skewnessDetection(originalImage=image)

    # reads the rotated image and crops out the boxed form and save in temporaryResults folder
    imageCropping(image=image)

    # reads XML and stores the dataframe inside temporaryResults folder
    templateMatcher(formSide=form_side)

    # reading image to preprocess.
    img = cv2.imread("../temporaryResults/cropped.jpg", 0)

    # This method saves final preprocessed output file to temporaryResults folder
    preprocess(img_grey=img)

    # Segments the form image and save it in local directory
    imageSegmentation(userId=user_id)

    # detects checkboxes from the images segmented into folders.
    checkboxes = checkboxDetection(side=form_side)

    # stitching the image in folders
    imageStitching(userId=user_id)

    # detecting the text form the image
    ls = documentDetection(userId=user_id,form_side=form_side)
    final_json = dict()
    for i in ls:
        #     print(i)
        #     print('')
        final_json[i['field'] + '_CONFIDENCE'] = i['word_confidence']
        final_json[i['field']] = i['word_text']
    final_json.update(checkboxes)
    pprint(final_json)
    return final_json


if __name__ == '__main__':
    main(form_side="front", user_id="BANDANA")
