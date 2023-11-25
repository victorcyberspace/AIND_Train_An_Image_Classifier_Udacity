#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
                                                                       
# PROGRAMMER: Asiimwe Victor Emmanuel 
# DATE CREATED: 06/24/23
# REVISED DATE: 07/12/23

"""
The purpose of this code block is to get the input arguments from the command line. 
The code first imports the argparse module, which is used to parse command line arguments. 
Then, the get_input_args() function is defined. This function creates an ArgumentParser 
object and adds three arguments: --dir: The directory path to the pet images.
--arch: The CNN Model architecture for use, --dogfile: The dog file with names.
The get_input_args() function then returns the parsed arguments
"""


# Import the argparse module
import argparse

# Define the get_input_args() function
def get_input_args():

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add the --dir argument
    parser.add_argument('--dir', type = str, default = 'pet_images', help = 'directory path to pet images')

    # Add the --arch argument
    parser.add_argument('--arch', type = str, default = 'resnet', help = 'CNN Model architecture for use')

    # Add the --dogfile argument
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'dog file with names')    

    # Return the parsed arguments
    return parser.parse_args()
