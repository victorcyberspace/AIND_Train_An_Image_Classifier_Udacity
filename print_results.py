#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py                                                                           
# PROGRAMMER: Asiimwe Victor Emmanuel 
# DATE CREATED: 06/30/23
# REVISED DATE: 07/12/23


def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    
    """
    This function prints the results of the classification experiment.

    Args:
    results_dic: A dictionary of results.
    results_stats_dic: A dictionary of statistics.
    model: The name of the CNN model.
    print_incorrect_dogs: Whether to print incorrect dog/not dog assignments.
    print_incorrect_breed: Whether to print incorrect dog breed assignments.

    """

    # Print the header.
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(),"***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format("N Not-Dog Images:", results_stats_dic['n_notdogs_img']))
    print(" ")

# Print the precision, recall, and f1-score for dogs and not-dogs.
    for key in results_stats_dic:
        if key.startswith('p'):
            print(key, ":", results_stats_dic[key])

# Print the incorrect dog/not dog assignments if requested.
    if print_incorrect_dogs:
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print("Pet Label:", results_dic[key][0])
                print("Classifier Label:", results_dic[key][1])

# Print the incorrect dog breed assignments if requested.
    if print_incorrect_breed:
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))
"""
The print_results function takes a dictionary of results and a dictionary of statistics as input, 
and prints a summary of the results. The function first prints the header, which includes the 
number of images, the number of dog images, and the number of not-dog images. The function 
then prints the precision, recall, and f1-score for dogs and not-dogs. If the user has 
requested it, the function will also print the incorrect dog/not dog assignments and the incorrect 
dog breed assignments.The purpose of the print_results function is to provide a summary of 
the results of the classification experiment. This information can be used to assess the performance
of the CNN model and to identify areas for improvement.
"""
