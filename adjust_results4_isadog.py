#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Amal AbuHmoud
# DATE CREATED: 24/5/2024                                
# REVISED DATE: 24/5/2024
# 
def adjust_results4_isadog(results_dic, dogfile):       
    dognames_dic = {}
    try:
        with open(dogfile, 'r') as file:
            for line in file:
              dogname = line.rstrip()
              if dogname not in dognames_dic:
                dognames_dic[dogname] = 1
              else:
                print("Warning: dogname already exists in the dictionary.") 
    except FileNotFoundError:
        print(f"File '{dogfile}' not found.")

    for value in results_dic.values():
      if value[0] in dognames_dic:
        value.append(1) # is a dog
      else:        
        value.append(0) # is not a dog
      if value[1] in dognames_dic:
        value.append(1) # classifier says it is a dog
      else:        
        value.append(0) # classifier says it is not a dog
