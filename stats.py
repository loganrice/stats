from scipy import stats
import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

columns = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=columns)
df['Alcohol'] = df['Alcohol'].astype('float')
df['Tobacco'] = df['Tobacco'].astype('float')

# mean
print "The mean for the Alcohol dataset is {}".format(df['Alcohol'].mean())
print "The mean for the Tobacco dataset is {}".format(df['Tobacco'].mean())

# median, 
print "The median for the Alcohol dataset is {}".format(df['Alcohol'].median())
print "The median for the Tobacco dataset is {}".format(df['Tobacco'].median())

# mode, 
print "The mode for the Alcohol dataset is {}".format(stats.mode(df['Alcohol'])[0])
print "The mode for the Tobacco dataset is {}".format(stats.mode(df['Tobacco'])[0])

# range, 
alcohol_range = df['Alcohol'].max() - df['Alcohol'].min() 
tobacco_range = df['Tobacco'].max() - df['Tobacco'].min() 
print "The range for the Alcohol dataset is {}".format(alcohol_range)
print "The range for the Tobacco dataset is {}".format(tobacco_range)

# variance,
print "The variance for the Alcohol dataset is {}".format(df['Alcohol'].var())
print "The variance for the Tobacco dataset is {}".format(df['Tobacco'].var())

# standard deviation 
print "The standard deviation for the Alcohol dataset is {}".format(df['Alcohol'].std())
print "The standard deviation for the Tobacco dataset is {}".format(df['Tobacco'].std())

