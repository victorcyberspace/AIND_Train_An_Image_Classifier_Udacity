#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#     

# PROGRAMMER: Asiimwe Victor Emmanuel 
# DATE CREATED: 07/10/23                             
# REVISED DATE: 07/12/23

"""
PURPOSE: The code block adjust_results4_isadog() is used to adjust the results dictionary 
to include an isadog key with a value of 1 if the classifier label is a dog breed and the 
pet label is also a dog breed, or a value of 0 otherwise.
The code first creates a dictionary of dog breeds by reading a file containing a list of 
dog breeds. Then, the code iterates through the results dictionary and checks if the classifier 
label and pet label are both # dog breeds. If they are, the code sets the isadog key to 1. 
Otherwise, the code sets the isadog key to 0.
The purpose of this code is to provide a more accurate assessment of whether a dog image is 
actually a dog. By checking if both the classifier label and pet label are dog breeds, the 
code can reduce the number of false positives.
"""

def adjust_results4_isadog(results_dic, dogfile):
    # Create a dictionary of dog breeds.
    dognames_dic = dict()
    with open(dogfile, "r") as infile:
        line = infile.readline()
        while line != "":
            line = line.strip()
            if line not in dognames_dic:
                dognames_dic[line] = 1
            line = infile.readline()

    # Iterate through the results dictionary.
    for key in results_dic:
        # If the classifier label is a dog breed,
        if results_dic[key][0] in dognames_dic:
            # If the pet label is also a dog breed,
            if results_dic[key][1] in dognames_dic:
                # Set the isadog key to 1.
                results_dic[key].extend((1, 1))
            # Otherwise, set the isadog key to 0.
            else:
                results_dic[key].extend((1, 0))
        # Otherwise,
        else:
            # If the pet label is a dog breed,
            if results_dic[key][1] in dognames_dic:
                # Set the isadog key to 0.
                results_dic[key].extend((0, 1))
            # Otherwise, set the isadog key to 0.
            else:
                results_dic[key].extend((0, 0))