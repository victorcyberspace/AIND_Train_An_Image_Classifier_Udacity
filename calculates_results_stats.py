#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
                                                                        
# PROGRAMMER: Asiimwe Victor Emmanuel 
# DATE CREATED: 07/07/23                                
# REVISED DATE: 07/12/23

"""
Purpose of the code:
The code calculates the following statistics for the results of the dog classifier:
The number of images classified as dogs
The number of images classified as not dogs
The number of images that were correctly classified
The percentage of images that were correctly classified
The percentage of dog images that were correctly classified
The percentage of not dog images that were correctly classified
The percentage of dog images that were correctly classified, including the breed
The code iterates over the results dictionary and increments the appropriate counters for each image. The # percentage statistics are then calculated by dividing the appropriate counter by the total number of 
images. The code returns a dictionary containing the results statistics. 
This dictionary can then be used to analyze the performance of the dog classifier.
"""

def calculates_results_stats(results_dic):
    # Initialize a dictionary to store the results statistics.
    results_stats_dic = {
        'n_images': len(results_dic),
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'pct_match': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_notdogs': 0.0
    }

    # Iterate over the results dictionary.
    for key in results_dic:

        # If the image is a dog, increment the number of dog images 
        # and the number of correct dog classifications.
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
                if results_dic[key][2] == 1:
                    results_stats_dic['n_correct_breed'] += 1

        # Otherwise, the image is not a dog, so increment the number 
        # of not dog images and the number of correct not dog classifications.
        else:
            results_stats_dic['n_notdogs_img'] += 1
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

        # If the classifier correctly identified the breed of the dog, 
        # increment the number of correct breed classifications.
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

    # Calculate the percentage of images that were correctly classified.
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / len(results_dic)) * 100.0

    # Calculate the percentage of dog images that were correctly classified.
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0

    # Calculate the percentage of not dog images that were correctly classified.
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0

    # Calculate the percentage of dog images that 
    # were correctly classified, including the breed.
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0

    return results_stats_dic

