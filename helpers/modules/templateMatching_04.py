# importing libraries
import cv2
import pandas as pd
import xml.etree.ElementTree as ET


def templateMatcher(formSide):
    front_template_file = 'XMLs/frontTemplate.xml'
    back_template_file = 'XMLs/backTemplate.xml'

    if formSide == '1':
        template_file = front_template_file
    else:
        template_file = back_template_file
    # template_file = front_template_file
    # empty list
    dumps = list()

    # contains the annotations form the template file being used
    annotations = template_file
    # print("Annotations : {}".format(annotations))
    # opening the template XML file
    in_file = open(template_file)

    # print("in file {}".format(in_file))
    # tree structure of the template file
    tree = ET.parse(in_file)
    # print("Tree : {}".format(tree))
    # root element of the tree i.e. starting of the XML tree
    root = tree.getroot()

    # image file name as mentioned in the XML file
    jpg = annotations.split ('.')[0] + '.jpg'
    # Image Size as mentioned in the XML file
    imsize = root.find('size')

    # Width and Height of the Image as mentioned in the XML Tree
    image = cv2.imread("temporaryResults/cropped"+formSide+".jpg", 0)
    # w = int(imsize.find('width').text)
    # h = int(imsize.find('height').text)
    w = image.shape[1]
    h = image.shape[0]

    # Empty list
    all = list()
    # Loop that saves all the information about a field in the "all" list
    for obj in root.iter('object'):
        current = list()
        name = obj.find('name').text
        folder = obj.find('folder').text
        xmlbox = obj.find('bndbox')
        xn = int(float(xmlbox.find ('xmin').text))
        xx = int(float(xmlbox.find ('xmax').text))
        yn = int(float(xmlbox.find ('ymin').text))
        yx = int(float(xmlbox.find ('ymax').text))
        current += [jpg, w, h, name, folder, xn, yn, xx, yx]
        all += [current]
    data = pd.DataFrame(all, columns = ['path', 'width', 'height', 'label', 'folder', 'xmin', 'ymin', 'xmax', 'ymax'])
    data.to_csv("temporaryResults/templateMatcher_data.csv")
    # Closing the template file
    in_file.close()
    print("[PROCESS COMPLETION]: Template Matching Completed..!")

# templateMatcher(formSide = "front")
