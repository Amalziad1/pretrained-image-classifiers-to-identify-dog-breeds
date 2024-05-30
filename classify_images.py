#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Amal AbuHmoud
# DATE CREATED: 23/5/2024                                
# REVISED DATE: 23/5/2024

from classifier import classifier 
import os

def classify_images(images_dir, results_dic, model):
    for filename,value in results_dic.items():
        image_path = os.path.join(images_dir, filename)
        classifier_label = classifier(image_path, model).lower().strip()
        pet_label = value[0]
        if pet_label in classifier_label:
            match = 1
        else:
            match = 0
        value.extend([classifier_label,match])
    