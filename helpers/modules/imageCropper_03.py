import cv2


def imageCropping(image, form_side):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, img_bin = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # print (img_bin)
    img_bin = 255 - img_bin
    # img_bin = cv2.bitwise_not(img_bin)
    cv2.imwrite("temporaryResults/binary_image.jpg", img_bin)  # [MAIN-RUN]
    print("[INFO]: Writing the binary image on disk...")

    # print(np.array(img).shape)

    # performing morphological operations

    kernel_length = 5
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    img_temp1 = cv2.erode(img_bin, vertical_kernel, iterations=10)
    vertical_lines_image = cv2.dilate(img_temp1, vertical_kernel, iterations=10)

    print("[INFO]: Writing the binary vertical lines image on disk...")
    cv2.imwrite("temporaryResults/binary_vertical_lines.jpg", vertical_lines_image)  # [INDIVIDUAL-FILE RUN]

    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=10)
    horizontal_lines_image = cv2.dilate(img_temp2, hori_kernel, iterations=10)

    print("[INFO]: Writing the binary horizontal lines image on disk...")
    cv2.imwrite("temporaryResults/binary_horizontal_lines.jpg", horizontal_lines_image)  # [INDIVIDUAL-FILE RUN]

    alpha, beta = 0.5, 1 - 0.5
    image_final_bin = cv2.addWeighted(vertical_lines_image, alpha, horizontal_lines_image, beta, 0.0)
    image_final_bin = cv2.erode(~image_final_bin, kernel, iterations=3)

    (thresh, image_final_bin) = cv2.threshold(image_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite("temporaryResults/final_binary_image.jpg", image_final_bin)  # [MAIN-RUN]
    print("[INFO]: Writing the final binary image file on disk...")

    contours, heirarchy = cv2.findContours(image_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, boundingBoxes = sort_contours(contours)  # , method = "top-to-bottom"

    idx = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        # print ("X: {0},Y: {1}, W: {2}, H: {3}".format (x, y, w, h))
        if w > 4000 and h > 5000:
        # if w > 2000 and h > 3000:
            # print ("X: {0},Y: {1}, W: {2}, H: {3}".format (x, y, w, h))
            idx += 1
            new_img = gray_img[y:y + h, x:x + w]
            # cv2.imwrite("temporaryResults/cropped.jpg", new_img)  # main
            cv2.imwrite("temporaryResults/cropped" + form_side + ".jpg", new_img)  # [INDIVIDUAL-FILE RUN]
            print("[INFO]: File Cropped..!")

            # throw error if image has any black line in image
            if w < 4000 and h > 6000:
                print("[ERROR]: This image has potential chances of containing a black line in between of the image.")
            if w > 4000 and h < 4000:
                print("[ERROR]: This image has potential chances of containing a black line in between of the image")

    print("[PROCESS COMPLETION]: Image Cropping Completed..")


# Contour Sorting
def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes), key=lambda b:b[1][i], reverse=reverse))
    return cnts, boundingBoxes

# image = cv2.imread ("../formImages/front/Sarita_front.jpg")
# imageCropping (gray_img = image )
