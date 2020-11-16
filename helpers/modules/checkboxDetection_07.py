import numpy as np
import cv2
import os


def checkboxDetection(side, user_id):
    mainDict = dict()
    front_form_checkbox_folders = [
        'gender',
        'number_of_brothers_sisters',
        'religion',
        'category',
        'special_cases',
        'talent_areas',
        'awards',
        'present_class',
        'present_class_stream',
        'mode_of_course',
        'type_of_student'
    ]

    back_form_checkbox_folders = [
        'class_10_board',
        'class_12_board',
        'class_12_stream',
        'graduation_stream',
        'graduation_course_duration',
        'post_graduation_stream',
        'post_graduation_course_duration',
        'no_bank_account'
    ]
    rootDir = "temporaryResults/imageSegmented/"

    if side == '1':
        checkbox_folders = front_form_checkbox_folders
    else:
        checkbox_folders = back_form_checkbox_folders
    for i in checkbox_folders:
        folderPath = rootDir + user_id + "/" + str(i)
        #     print(folderPath)

        for complete_path, directories, files in os.walk(folderPath):
            #     print("Complete Path: {}".format(complete_path))
            #         print("directories: {}".format(directories))
            #     print("Files: {}".format(files))
            for filename in files:
                #             print("Filename: {}\n".format(filename))
                file_complete_path = folderPath + "/" + filename
                #             print("file to read: {}\n".format(file_complete_path))
                image = cv2.imread(file_complete_path)

                temp = np.sum(image == 255)
                #             print(temp)
                if temp > 3000:
                    createCheckbox = True
                    headOfCompletePath, tailOfCompletePath = os.path.split (file_complete_path)
                    #                 print("head: {}".format(headOfCompletePath))
                    #                 print("tail: {}".format(tailOfCompletePath))
                    actual_folder = headOfCompletePath.rsplit ("/")[-1]
                    actual_value = (tailOfCompletePath.rsplit (".")[0]).rsplit("_")[-1]
                    #                 print("Actual Folder: {}".format(actual_folder))
                    #                 print("Actual Value : {}".format(actual_value))

                    # append value if folder already exists
                    if actual_folder in mainDict.keys ():
                        mainDict[actual_folder] += "," + actual_value
                    else:
                        mainDict[actual_folder] = actual_value

                    mainDict[actual_folder + "_CONFIDENCE"] = 1.0
    print("[PROCESS COMPLETION]: Checkbox Detection Complete..!")
    return mainDict
