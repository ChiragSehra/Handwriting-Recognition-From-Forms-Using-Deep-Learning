import cv2
import os
import pandas as pd


def imageSegmentation(userId):
    img = cv2.imread("temporaryResults/output.png")
    data = pd.read_csv("temporaryResults/templateMatcher_data.csv")
    for i, row in data.iterrows():
        x1 = row['xmin']
        y1 = row['ymin']
        x2 = row['xmax']
        y2 = row['ymax']
        #     print("Coodinates: {0},{1},{2},{3}".format(x1,y1,x2,y2))
        image = img[y1:y2, x1:x2]
        # print("Shape of new Image is: {}".format(img.shape))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh, bnw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        path1 = row.folder
        image_path = row.label
        crop_folder_path = 'temporaryResults/imageSegmented/' + str(userId) + '/' + path1
        crop_image_path = crop_folder_path + '/' + image_path + '.jpg'
        #     print(image_path)
        #     print("path1: "+str(path1))
        #     print("crop_folder_path is: "+str(crop_folder_path))
        #     print("crop_image_path is :"+str(crop_image_path))
        if os.path.exists(crop_folder_path):
            # print('[INFO]: Image is segmented into {0} directory'.format(crop_folder_path))
            cv2.imwrite(crop_image_path, bnw)
        if not os.path.exists(crop_folder_path):
            # print("[INFO]: Creation of directory {0} successful".format(crop_folder_path))
            original_umask = os.umask(0)
            os.makedirs(crop_folder_path, 0o777)
            os.umask(original_umask)
            # print('[INFO]: Image is segmented into {0} directory'.format(crop_folder_path))
            cv2.imwrite(crop_image_path, bnw)
    print("[PROCESS COMPLETION]: Image Segmentation Complete..!")
