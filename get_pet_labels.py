#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
                                                                           
# PROGRAMMER: Asiimwe Victor Emmanuel
# DATE CREATED: 06/30/23                                
# REVISED DATE: 07/12/23

"""
The function works by first iterating over the files in the image directory. For each file, 
the function checks if the file starts with a period. If the file does not start with a period, 
the function then gets the filename of the image. The function then initializes a pet name variable 
and iterates over the words in the filename. For each word, the function checks if the word is a 
valid pet name. If the word is a valid pet name, the function adds the word to the pet name variable.
The function then strips any whitespace from the pet name variable and adds the filename to the 
dictionary with the pet name as the value.
"""
# import the 'os' and 're' modules
import os
import re

def get_pet_labels(image_dir):
    results_dic = {}

    # Iterate over the files in the image directory.
    for file in os.listdir(image_dir):

        # Ignore files that start with a period.
        if not file.startswith("."):

            # Get the filename of the image.
            file_name = os.path.basename(file)

            # Initialize a pet name variable.
            pet_name = ""

            # Iterate over the words in the filename.
            for word in file_name.lower().split("_"):

                # Check if the word is a valid pet name.
                if re.compile(r"^[a-zA-Z]+$").match(word):

                    # Add the word to the pet name variable.
                    pet_name += word + " "

            # Strip any whitespace from the pet name variable.
            pet_name = pet_name.strip()

            # If the filename is not already in the dictionary, add it with the
            # pet name as the value.
            if file_name not in results_dic:
                results_dic[file_name] = [pet_name]
            # Otherwise, print a warning message.
            else:
                print("** Warning: Duplicate files exist in directory ----> ", file_name)

    return results_dic


