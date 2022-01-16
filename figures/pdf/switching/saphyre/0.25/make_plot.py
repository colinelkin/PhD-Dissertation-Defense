import csv, numpy
from sklearn import utils
import matplotlib.pyplot as plt

def get_data(filename, scaled, io, ind=[]):
	with open(filename) as f:
		reader = csv.reader(f)
		data = []
		for line in reader:
			data.append(line)
		return data				
						
						
						
str_output_data1 = get_data("single_results_by_time.csv",True,False)
float_output_data1 = [[float(j) for j in i] for i in str_output_data1]
#output_data1 = numpy.zeros((len(float_output_data1),2))
#output_data1 = [[int(j) for j in i] for i in float_output_data1]
#output_data1 = utils.validation.column_or_1d(output_data1)

str_output_data2 = get_data("dyn_results_by_time.csv",True,False)
float_output_data2 = [[float(j) for j in i] for i in str_output_data2]
#output_data2 = [[int(j) for j in i] for i in float_output_data2]
#output_data2 = utils.validation.column_or_1d(output_data2)
output_data1 = numpy.array(float_output_data1)
output_data2 = numpy.array(float_output_data2)

a1 = len(output_data1) * 3 + 1
a2 = len(output_data1) * 4
xrange = range(a1, a2)
yrange = 100 * (1 - output_data1[1:,0])
yrange2 = 100 * (1 - output_data2[1:,0])

plt.plot(xrange, yrange, linestyle = 'dashed', label = 'single method selection')
plt.xlabel("sample number")
plt.ylabel("validation error (%)")
#plt.savefig(filename + "1.png")
#plt.figure()
plt.plot(xrange, yrange2, label = 'dynamic method selection')
plt.legend(loc = 'upper right')
plt.savefig("saphyre25.png")
plt.close('all')