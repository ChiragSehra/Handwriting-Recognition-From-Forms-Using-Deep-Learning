# Handwriting Recognition from Forms using Computer Vision and Deep Learning
This is a Handwriting recognition system that helps in extracting out information from forms filled by students for scholarships and saving to database for searchable format.

## PROPOSED METHOD

All these forms are filled physically by the operator and are
sent across via email, eventually depreciating and blemishing
the image. This introduces a lot of noise in form image. Due
to this, algorithm has to be dynamic and hefty to cacophony.
The form registration also has to be very accurate since the
accuracy of the field image extraction and hence field
recognition depends on it.

![](/docs/static/img/proposed-methodoly.png?raw=true)

-   **Accessing the Images**: The process starts with reading the image from the S3 location. A scanned image in `jpg` format is uploaded to S3 location. The image is scanned at 600dpi to ensure pixels of the characters in the image are clear to achieve maximum accuracy.
-   **Image Correction**: It involves correcting the asymmetry in the image. This is achieved by converting the image to `grayscale` format and then thresholding it. The image is thresholded with binary filter, a rotated rectangle of the minimum area in the image is found followed by calculation of an `affine` matrix of 2D rotation. The image is then rotated in the opposite direction from the base angle which straightens the image.

![](/docs/static/img/image-correction.png?raw=true)

-   **Image Cropping**: The form image is converted to binary format. All the vertical and horizontal lines are extracted from the image and a mesh like structure is created. Contour detection is used to extract the contours from the processed image. The contour with the largest area is extracted out which is the bounding box around main entries.

    ![](/docs/static/img/image-cropping.png?raw=true)

-   **Template Matching**: n XML file is created both for the front and back side of the form. XML file contains the information about the boxes in the image and the coordinates associated with them. It also contains the meta-information of the image like the width and height of the image, its path and name. This well-formulated structure property of XML allow to easily extracting information. Thus, a tree-like-structure is created with all the basic information.

  ![](/docs/static/img/template-matching.png?raw=true)

## IMAGE PROCESSING

It involves noise removal, erosion and dilation of image. The main aim of pre-processing is to improve the image quality so that features of the image are enhanced. The cropped form image is threshold-ed into binary format. It is then eroded with a 2x2 kernel. Adaptive Mean Threshold is used for thresholding the image. A horizontal kernel is created with specified erosion and dilation of the image. Similarly, a vertical kernel is also created. These kernels are then used for producing masked images. These masked images are then stacked onto each other. It is then followed by a process of advanced morphological transformations.

  ![](/docs/static/img/image-processing-process.png?raw=true)

## IMAGE SEGMENTATION

With the structure created in template matching step, each field in the image (irrelevant of its type) is segmented into folder structure with folder name as the field name and having all the entries of each box of the entries as the files of that folder. For example: first name field is extracted from the form and each letter of the first name is segmented in a folder named first name in the directory.

![](/docs/static/img/image-segmentation.png?raw=true)

## INFORMATION EXTRACTION

-   **Check-box Detection**: It refers to extracting the information from the check-box field present in the form image. Since, all the fields are segmented down and stored into a directory, check-box fields becomes easily accessible. All the available options of the check-box fields are fed into the algorithm and the pixel values of each image is analyzed. Pixel count in the image can give us an idea of the stroke made in the check-box. As an example, an ‘x’ in the check-box will have more amounts of white pixels rather than an image with no ‘x’ marked. Thus, total number of white pixels in the image is calculated and fields are marked where the check-box value has white pixels over a specific threshold value. This way, information from the check-box field is extracted.

## IMAGE STITCHING

Image stitching refers to the process of combining images in order that form up a complete field value. Each box inside any field has specific dimensions of 90 x 109 pixels. All the folders which are text fields are parsed and all the images inside the folders are stitched in orderly fashion and are saved in the same folder

## CHARACTER DETECTION

-   **Text and Numeric Field Detection**: All the text fields taken into account are alphabetical and alphanumeric characters. The Vision API uses DOCUMENT_TEXT_DETECTION to detect handwriting from an image or file. The `JSON` response contains several information like the page, paragraphs, blocks, words and information about where a break occurs in the dense text in image. There are several languages that Google Vision supports. By default, Vision API uses automatic language detection.
    Google vision requires calling an `ImageAnnotatorClient` method with service account credentials passed to it as parameters of the method. All the fields are recursively read from the folder structure created and the `JSON` response is intelligently parsed and the information required is stored in another `JSON` object which contains the text_field_name, word_text and word_confidence.
    For numeric fields, a started machine learning model trained upon MNIST is used. As the testing dataset increases, the folders containing numeric fields, are shifted to training dataset for continuous training of model on the incoming dataset. This ensures, more handwritten patterns are taken into account.

# Process flow of Application

-   The standard image size used for training and testing purposes is 90 x 109 pixels equivalent to 9810 different features.
-   Variation in range of pixel values of the image is between 0 and 255 pixels.
-   The number of iterations are increased and adjusted as per the increase in accuracy of the model.
-   One hot vector of the target labels are fed into the network.
-   Complete dataset is divided into training and testing data in ratio of 80: 20.
-   The training data consists of handwritten samples of digit fields only i.e. from 0 to 9.
-   Weights of different models received after training network are saved.
-   Bottleneck weights of the network are available and a final classification layer with 10 classification neuron nodes are added as a layer. This layer is trained over the bottleneck structure.
-   The weights and biases are adjusted according to the dataset.
-   Training is done on 100 epochs for 5 batches.
-   The model is saved and tested on test-data set.

![](/docs/static/img/process-flow-of-application.png?raw=true)
