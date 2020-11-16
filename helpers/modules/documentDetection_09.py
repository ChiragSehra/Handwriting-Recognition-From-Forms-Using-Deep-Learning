from google.cloud import vision
import io
import os
from google.oauth2 import service_account
import cv2
import numpy as np
import unicodedata
import re

all_json = list()


def detect_document(path):
    """
    Detects document features in an image.
    Arguments:
        path: path to the image file for which characters has to be detected
    """

    creds = service_account.Credentials.from_service_account_file('credentials/Character Detection-208f08e77e7d.json')
    client = vision.ImageAnnotatorClient(
        credentials=creds
    )

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    field = path.rsplit("/")[-2]
    image = vision.types.Image(content=content)
    all_blocks = []
    response = client.document_text_detection(image=image)
    #     print(client)
    #     print("Response: {}".format(response))

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            block_info = {"Block_Confidence": block.confidence, "Paragraphs": []}
            #             print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                paragraph_info = {"Paragraph_Confidence": paragraph.confidence, "Words": []}
                #                 print('Paragraph confidence: {}'.format(
                #                     paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    word_info = {"Word_Text": word_text, "Word_Confidence": word.confidence, "Symbols": []}

                    #                     print('Word text: {} (confidence: {})'.format(
                    #                         word_text, word.confidence))

                    for symbol in word.symbols:
                        symbol_info = {'Symbol_Text': symbol.text, 'Symbol_Confidence': symbol.confidence}
                        word_info["Symbols"].append(symbol_info)
                    #                         print('\tSymbol: {} (confidence: {})'.format(
                    #                             symbol.text, symbol.confidence))

                    paragraph_info["Words"].append(word_info)
                block_info["Paragraphs"].append(paragraph_info)
            all_blocks.append(block_info)

    data_list = []

    for rows in all_blocks:
        result = {}
        #         if "Block_Confidence" in rows and rows["Block_Confidence"]:
        #             result["block_confidence"] = rows["Block_Confidence"]
        if "Paragraphs" in rows and len(rows["Paragraphs"]) > 0:
            for paragraphs in rows["Paragraphs"]:
                if "Words" in paragraphs and len(paragraphs["Words"]) > 0:
                    word_confidence = []
                    word_text = []
                    for words in paragraphs["Words"]:
                        if "Word_Confidence" in words and words["Word_Confidence"] is not None:
                            word_confidence.append(words["Word_Confidence"])
                        if "Word_Text" in words and words["Word_Text"] is not None:
                            word_text.append(words["Word_Text"])
                result["word_confidence"] = min(word_confidence)
                result["word_text"] = "_".join(word_text)
                result["field"] = field
        data_list.append(result)
    #     print(data_list)
    fields = np.unique(([li['field'] for li in data_list]))

    word_text = list([li['word_text'] for li in data_list])
    # average word confidence
    word_confidences = sum([li['word_confidence'] for li in data_list]) / len(
        [li['word_confidence'] for li in data_list])
    final_word_text = ''.join(word_text)

    result['field'] = fields[0]
    s = unicodedata.normalize('NFKD', final_word_text).encode('ascii', 'ignore')
    s = s.decode('utf-8')
    result['word_text'] = re.sub(r"[^a-zA-Z0-9]+", ' ', s).strip()
    result['word_confidence'] = word_confidences

    # all_json.append (result.copy ())
    # # print (result)

    return result


def documentDetection(userId, form_side):
    l = []
    front_folder_list = [
        'first_name', 'last_name', 'date_of_birth', 'aadhar_number', 'present_address', 'student_mobile_number', 'email', 'disability',
        'percentage_of_disability', 'father_first_name', 'father_last_name', 'father_occupation', 'father_mobile_number', 'father_annual_income',
        'father_email_id', 'mother_first_name', 'mother_last_name', 'mother_occupation', 'mother_annual_income', 'mother_email_id',
        'mother_mobile_number', 'annual_fee', 'previous_class_passing_year', 'marks_obtained', 'total_marks'
    ]
    back_folder_list = [
        'class_10_passing_year', 'class_10_total_marks', 'class_10_marks_obtained', 'class_12_passing_year', 'class_12_total_marks',
        'class_12_marks_obtained', 'graduation_total_marks', 'graduation_marks_obtained', 'graduation_passing_year', 'post_graduation_total_marks',
        'post_graduation_marks_obtained', 'post_graduation_passing_year', 'bank_name', 'ifsc_code', 'account_number', 'account_holder_name',
        'relation_with_account_holder'
    ]
    # user_id = url.rsplit("/")[-2]
    user_id = userId
    # user_id = "Sarita"
    rootDir = "temporaryResults/imageSegmented/" + user_id + "/"

    # creating a list of folders that exist in the root directory
    folderList = []
    imageFiles = []
    if form_side == "1":
        folderList = front_folder_list
    if form_side == "2":
        folderList = back_folder_list

    # #creatng a list of images that have the same name as folder name i.e. the files that have been stitched
    # print(folderInPath)
    for a in folderList:
        a = a + ".jpg"
        #     print(a)
        imageFiles.append(a)

    # print("imageFiles contain: {}".format(imageFiles))

    # print(imageFiles)
    ls = []
    for a, b, c in os.walk(rootDir):
        for i in imageFiles:
            if i in c:
                try:
                    img = cv2.imread(a + '/' + i)
                    #             plt.figure()
                    #             plt.imshow(img)
                    #                 print(i.rsplit(".")[0])
                    ls.append(detect_document(a + '/' + i))

                except Exception as ex:
                    # print("Field Not Detected..!")
                    print(str("Vision API returned null..!"))
    return ls
