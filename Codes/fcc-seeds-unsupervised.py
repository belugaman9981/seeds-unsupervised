import numpy             as np
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt


cols = ["area", "perimeter", "compactness", "length", 
        "width", "asymmetry", "groove", "class"]

df = pd.read_csv("seeds_dataset.txt", 
                 names= cols, sep= "\s+")

df.head()


for i in range(len(cols)-1):
  for j in range(i + 1, len(cols) - 1):
    x_label = cols[i]
    y_label = cols[j]
    sns.scatterplot(x= x_label, y= y_label, data= df, hue= 'class')
    plt.show()
    
