# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os

filepath = os.path.join(os.getcwd(), 'data', 'Most_Popular_Baby_Boy_Names__1980-2013.csv')

nameData = pd.read_csv(filepath)