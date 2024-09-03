import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\r00_env_START\boston.csv', index_col=0)

# Create a jointplot for DIS and NOX
sns.jointplot(x='DIS', y='NOX', data=data, kind='reg', height=8)

# Add a title to the plot
plt.suptitle('Joint Plot of Distance to Employment (DIS) vs Pollution (NOX)', y=1.03)

# Save the plot as a file
plt.savefig(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\dis_nox_jointplot.png')


