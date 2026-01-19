import numpy             as np
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt


cols = ["area", "perimeter", "compactness", "length", 
        "width", "asymmetry", "groove", "class"]

df = pd.read_csv("seeds_dataset.txt", 
                 names= cols, sep= "\s+")

