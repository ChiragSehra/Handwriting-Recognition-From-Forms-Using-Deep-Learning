import numpy as np
import cv2
import os


# rootDir = "temporaryResults/imageSegmented/"
# user_id = "Sarita"

def imageStitching(user_id, form_side):
    try:
        rootDir = "temporaryResults/imageSegmented/"
        front_folders_93_108 = ['first_name', 'last_name', 'aadhar_number', 'present_address', 'student_mobile_number',
                                'email', 'disability', 'percentage_of_disability', 'father_first_name', 'father_last_name',
                                'father_occupation', 'father_mobile_number', 'father_annual_income', 'father_email_id',
                                'mother_first_name', 'mother_last_name', 'mother_occupation', 'mother_mobile_number',
                                'mother_annual_income', 'mother_email_id', 'annual_fee', 'previous_class_passing_year',
                                'marks_obtained', 'total_marks']
        back_folders_95_112 = ['class_10_total_marks', 'class_10_marks_obtained', 'class_12_passing_year', 'class_12_total_marks',
                               'class_12_marks_obtained', 'graduation_total_marks', 'graduation_marks_obtained', 'graduation_passing_year',
                               'post_graduation_total_marks', 'post_graduation_marks_obtained', 'post_graduation_passing_year',
                               'bank_name', 'ifsc_code', 'account_number', 'account_holder_name', 'relation_with_account_holder'
                               ]
        if form_side == '1':
            for i in front_folders_93_108[:]:
                globalImage = np.zeros((93, 108))
                for a, b, c in os.walk(rootDir + user_id + "/" + i):
                    sortedList = sorted(c, key=lambda x: int(x.split('.')[0].split('_')[-1]))
                    #         print(sortedList)
                    for f in sortedList:
                        img = cv2.imread(rootDir + user_id + '/' + i + '/' + str(f), 0)
                        globalImage = np.concatenate((globalImage, img), axis=1)
                    #             plt.figure()
                    #             plt.imshow(globalImage)
                    #         print("file is being saved to: {}".format(rootDir+i+'/'+i))
                    cv2.imwrite(rootDir + user_id + '/' + i + '/' + i + '.jpg', globalImage)
                    print("[INFO]: Saving File to {}...".format(rootDir + user_id + '/' + i + '/' + i + '.jpg'))

        if form_side == '2':
            for i in back_folders_95_112[:]:
                globalImage = np.zeros((95, 112))
                for a, b, c in os.walk(rootDir + user_id + "/" + i):
                    sortedList = sorted(c, key=lambda x: int(x.split('.')[0].split('_')[-1]))
                    #         print(sortedList)
                    for f in sortedList:
                        img = cv2.imread(rootDir + user_id + '/' + i + '/' + str(f), 0)
                        globalImage = np.concatenate((globalImage, img), axis=1)
                    #             plt.figure()
                    #             plt.imshow(globalImage)
                    #         print("file is being saved to: {}".format(rootDir+i+'/'+i))
                    cv2.imwrite(rootDir + user_id + '/' + i + '/' + i + '.jpg', globalImage)
                    print("[INFO]: Saving File to {}...".format(rootDir + user_id + '/' + i + '/' + i + '.jpg'))

        folders_108_93 = ['date_of_birth']
        if form_side == '1':
            for i in folders_108_93[:]:
                globalImage = np.zeros((93, 108))
                for a, b, c in os.walk(rootDir + user_id + "/" + i):
                    sortedList = sorted(c, key=lambda x: int(x.split('.')[0].split('_')[-1]))
                    #         print(sortedList)
                    for f in sortedList:
                        img = cv2.imread(rootDir + user_id + '/' + i + '/' + str(f), 0)
                        globalImage = np.concatenate((globalImage, img), axis=1)
                    #             plt.figure()
                    #             plt.imshow(globalImage)
                    #         print("file is being saved to: {}".format(rootDir+i+'/'+i))
                    cv2.imwrite(rootDir + user_id + '/' + i + '/' + i + '.jpg', globalImage)
                    print("[INFO]: Saving File to {}...".format(rootDir + user_id + '/' + i + '/' + i + '.jpg'))
        print("[INFO]: IMAGE STITCHING COMPLETED..!")
    except Exception as e:
        raise Exception('Entry for user_id {0} already exists'.format(user_id))