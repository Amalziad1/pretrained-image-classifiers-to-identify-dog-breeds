#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Amal AbuHmoud
# DATE CREATED: 23/5/2024                                   

import argparse

# 
def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg',choices=['vgg','resnet','alexnet'], help='chosen CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file that contains dognames')
    
    return parser.parse_args()
