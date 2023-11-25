#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
                                                                             
# PROGRAMMER: Asiimwe Victor Emmanuel
# DATE CREATED: 06/19/23                                  
# REVISED DATE: 07/12/23

"""
This code block is the main entry point for the calculates_results_stats script. 
It starts by getting the input arguments from the command line, 
then checks them for validity. Next, it gets the pet labels 
for the images in the specified directory, then checks that 
they were created correctly.The code then classifies the images in 
the specified directory using the specified architecture, then 
checks that they were classified correctly. 
The code then adjusts the results to indicate whether or not 
each image is a dog, then checks that the results were adjusted correctly. 
The code then calculates the results statistics, then checks that 
they were calculated correctly. Finally, the code prints the results 
and results statistics.The purpose of this code block is to calculate 
the results statistics for the image classification task. 
The results statistics include the accuracy, precision, 
and recall for each class of images. 
The code block also prints the total elapsed runtime for the image classification task.
"""
# Imports python modules
from time import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():

    # Start a timer to measure the total runtime.
    start_time = time()

    # Get the input arguments from the command line.
    in_arg = get_input_args()

    # Check the command line arguments for validity.
    check_command_line_arguments(in_arg)

    # Get the pet labels for the images in the specified directory.
    results = get_pet_labels(in_arg.dir)

    # Check that the pet labels were created correctly.
    check_creating_pet_image_labels(results)

    # Classify the images in the specified directory using the specified architecture.
    classify_images(in_arg.dir, results, in_arg.arch)

    # Check that the images were classified correctly.
    check_classifying_images(results)

    # Adjust the results to indicate whether or not each image is a dog.
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check that the results were adjusted correctly.
    check_classifying_labels_as_dogs(results)

    # Calculate the results statistics.
    results_stats = calculates_results_stats(results)

    # Check that the results statistics were calculated correctly.
    check_calculating_results(results, results_stats)

    # Print the results and results statistics.
    print_results(results, results_stats, in_arg.arch, True, True)

    # Stop the timer and print the total runtime.
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )

if __name__ == "__main__":
    main()



