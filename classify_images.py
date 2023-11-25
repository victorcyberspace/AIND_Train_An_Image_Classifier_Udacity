#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
                                                                             
# PROGRAMMER: Asiimwe Victor Emmanuel 
# DATE CREATED: 07/08/23
# REVISED DATE: 07/12/23

"""
The purpose of this code block is to classify the images in the images_dir directory 
and add the results to the results_dic dictionary. The code first imports the classifier
function from the classifier module. Then, it defines the classify_images() function, 
which iterates over the filenames and pet labels in the results_dic dictionary. For each 
filename, the code gets the image path, uses the classifier function to classify the image, 
and converts the classifier label to lowercase and strips any whitespace. The code then 
creates a list of match indicators and iterates over the pet labels. For each pet label, 
the code adds a 1 to the match indicators list if the label is present in the classifier label, 
and a 0 if it is not present. Finally, the code adds the classifier label and the match 
indicators list to the results_dic dictionary.
"""

# Import the classifier function from the classifier module.
from classifier import classifier

# Define the classify_images() function.
def classify_images(images_dir, results_dic, model):

    # Iterate over the filenames and pet labels in the results dictionary.
    for filename, pet_label in results_dic.items():

        # Get the image path for the current filename.
        image_path = images_dir + '/' + filename

        # Use the classifier function to classify the image.
        classifier_label = classifier(image_path, model)

        # Convert the classifier label to lowercase and strip any whitespace.
        classifier_label = classifier_label.lower().strip()

        # initialize the match indicator to 0
        match_indicator = 0

        # Iterate over the pet labels and check if any label is present in the classifier label 
        for label in pet_label:
            if label in classifier_label:
                match_indicator = 1
                break

        # Add the classifier label and the match indicator to the results dictionary.
        results_dic[filename].extend([classifier_label] + [match_indicator])

"""
The classify_images() function is used to classify the images in the images_dir directory. 
The classifier function is a pre-trained classifier that can be used to classify images of 
dogs and cats. The match_indicators list is used to track the number of times each pet label
is present in the classifier label. The results_dic dictionary is used to store the results 
of the classification process. The code block is an important part of the calculates_results_stats 
script. The calculates_results_stats script is used to calculate the accuracy of the classifier 
and to generate a confusion matrix. The confusion matrix is a table that shows how often the classifier 
correctly classified the images and how often it incorrectly classified the images.
"""