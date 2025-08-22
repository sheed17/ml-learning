import seaborn as sns
#Scatterplots


"""sns.scatterplot(x="time", y="pulse", data=exercise, hue="kind", size="time")"""


#Histograms and Distribution Plots
"""
sns.histplot(exercise[‘pulse’], kde=True, bins=15)
sns.displot(exercise[‘pulse’], kde=True, bins=15)
"""

#Bar Plots
"""sns.barplot(x=”sex”, y=”tip”, data=tips)"""

#Strip Plot
"""sns.stripplot(x=”day”, y=”tip”, data=tips, hue=”sex”)"""


#Join Plot
"""sns.jointplot(x=”total_bill”, y=”tip”, data=tips, kind=”reg”)""" 

#Heat Maps
"""sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap=”coolwarm”)"""

print("Based on sns.get_dataset_names")