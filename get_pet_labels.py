#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Amal AbuHmoud
# DATE CREATED: 23/5/2024                                 
# REVISED DATE: 


from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    filenames = listdir(image_dir)
    for filename in filenames:
        if not filename.startswith('.'):
            words = filename.lower().strip().split('_')
            pet_label_words = " ".join([word for word in words if word.isalpha()])
            #adding filename to the dictionary if it does not exist
            if filename not in results_dic:
                results_dic[filename] = [pet_label_words]
            
    return results_dic
