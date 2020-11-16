from helpers.modules.urlToImage_01 import url_to_image
from helpers.modules.skewnessCorrection_02 import skewnessDetection
from helpers.modules.imageCropper_03 import imageCropping
from helpers.modules.templateMatching_04 import templateMatcher
from helpers.modules.preprocessing_05 import preprocess
from helpers.modules.imageSegmentation_06 import imageSegmentation
from helpers.modules.checkboxDetection_07 import checkboxDetection
from helpers.modules.imageStitching_08 import imageStitching
from helpers.modules.documentDetection_09 import documentDetection

import cv2
import string
import random
from pprint import pprint

alphabets_only = [
    'first_name', 'first_name_CONFIDENCE', 'last_name', 'last_name_CONFIDENCE', 'father_first_name',
    'father_first_name_CONFIDENCE', 'father_last_name', 'father_last_name_CONFIDENCE', 'father_occupation',
    'father_occupation_CONFIDENCE', 'mother_first_name', 'mother_first_name_CONFIDENCE', 'mother_last_name',
    'mother_last_name_CONFIDENCE', 'mother_occupation', 'mother_occupation_CONFIDENCE', 'bank_name',
    'bank_name_CONFIDENCE', 'account_holder_name', 'account_holder_name_CONFIDENCE'
]
numeric_only = [
    'date_of_birth', 'date_of_birth_CONFIDENCE', 'aadhar_number', 'aadhar_number_CONFIDENCE',
    'student_mobile_number', 'student_mobile_number_CONFIDENCE', 'percentage_of_disability',
    'percentage_of_disability_CONFIDENCE', 'father_mobile_number', 'father_mobile_number_CONFIDENCE',
    'father_annual_income', 'father_annual_income_CONFIDENCE', 'mother_mobile_number',
    'mother_mobile_number_CONFIDENCE', 'mother_annual_income', 'mother_annual_income_CONFIDENCE',
    'annual_fee', 'annual_fee_CONFIDENCE', 'previous_class_passing_year', 'previous_class_passing_year_CONFIDENCE',
    'marks_obtained', 'marks_obtained_CONFIDENCE', 'total_marks', 'total_marks_CONFIDENCE', 'class_10_total_marks',
    'class_10_total_marks_CONFIDENCE', 'class_10_marks_obtained', 'class_10_marks_obtained_CONFIDENCE',
    'class_12_passing_year', 'class_12_passing_year_CONFIDENCE', 'class_12_total_marks',
    'class_12_passing_year_CONFIDENCE', 'class_12_marks_obtained', 'class_12_marks_obtained_CONFIDENCE',
    'graduation_total_marks', 'graduation_total_marks_CONFIDENCE', 'graduation_marks_obtained',
    'graduation_marks_obtained_CONFIDENCE', 'graduation_passing_year', 'graduation_passing_year_CONFIDENCE',
    'post_graduation_total_marks', 'post_graduation_total_marks_CONFIDENCE', 'post_graduation_marks_obtained',
    'post_graduation_marks_obtained_CONFIDENCE', 'post_graduation_passing_year',
    'post_graduation_passing_year_CONFIDENCE', 'account_number', 'account_number_CONFIDENCE'
]


def main(s3_link, form_side, user_id):
    # returns image from s3 url

    image = url_to_image(s3_link)
    lettersAndDigits = string.ascii_letters + string.digits
    final_userId = ''.join(random.choice(lettersAndDigits) for i in range(6))
    user_id = final_userId

    # check for skewness and save a rotated image into temporaryResults folder
    skewness_angle = skewnessDetection(originalImage=image)

    # reads the rotated image and crops out the boxed form and save in temporaryResults folder
    imageCropping(image=image, form_side=form_side)

    # reads XML and stores the dataframe inside temporaryResults folder
    templateMatcher(formSide=form_side)

    # reading image to preprocess.
    img = cv2.imread("temporaryResults/cropped" + form_side + ".jpg", 0)

    # This method saves final preprocessed output file to temporaryResults folder
    preprocess(img_grey=img)

    # Segments the form image and save it in local directory
    imageSegmentation(userId=user_id)

    # detects checkboxes from the images segmented into folders.
    checkboxes = checkboxDetection(side=form_side, user_id=user_id)

    # stitching the image in folders
    imageStitching(user_id=user_id, form_side=form_side)

    # detecting the text form the image
    ls = documentDetection(userId=user_id, form_side=form_side)
    final_json = dict()
    skewness_json = dict()
    for i in ls:
        #     print(i)
        #     print('')
        final_json[i['field'] + '_CONFIDENCE'] = i['word_confidence']
        final_json[i['field']] = i['word_text']
    final_json.update(checkboxes)
    # pprint(final_json)
    for i in alphabets_only:
        if i in final_json:

            if i.rsplit("_")[-1] == "CONFIDENCE":
                final_json[i] = final_json[i] / 3
                print(i)
            else:
                # print(i)
                result = ''.join([j for j in final_json[i] if not j.isdigit()]).strip()
                #         print(result_text+"\n")
                final_json[i] = result

    for i in numeric_only:
        if i in final_json:
            #         print(i)
            #         print("Original Value: {}".format(processed_json[i]))

            if i.rsplit("_")[-1] == "CONFIDENCE":
                final_json[i] = final_json[i] / 3
            else:
                result = ''.join([j for j in final_json[i] if not j.isalpha()]).strip()
                #         print("Trimmed Value: {}\n".format(result))
                final_json[i] = result

    # final_json['user_id'] = user_id
    # final_json['user_document_library_id'] = user_document_library_id
    # final_json['document_type'] = form_side
    # final_json['form_url'] = s3_link

    skewness_json["rotation_angle"] = skewness_angle
    skewness_json["user_id"] = user_id
    skewness_json["document_type"] = form_side
    print("Final JSON is : {}".format(final_json))
    print("Rotation Angle is: {}".format(skewness_json))
    return final_json, skewness_json


if __name__ == '__main__':
    main()
