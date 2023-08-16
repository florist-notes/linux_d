#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:07:41 2021

@author: skk
"""

import os
fileDir = r"./"
fileExt = r".geojson"
files = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

import json
import random
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import multilinestring
multil = multilinestring.MultiLineString

for file in files:
    with open(file, encoding='utf-8') as f:
        layername = json.load(f)
    zip_codes = []    
    failed_zip = []
    for xzipno in range(len(layername['features'])):
        try:
            if layername['features'][xzipno]['properties']['zip'] != None:
                print(layername['features'][xzipno]['properties']['zip']) 
                zip_code = layername['features'][xzipno]['properties']['zip']
                zip_codes.append(zip_code)
        except KeyError:
            print('exception occured >>> failed at : '+str(xzipno))
            failed_zip.append(xzipno) #34275
    print(' ZIP codes of layer '+layername+' : ')
    print(set(zip_codes))
    
    
