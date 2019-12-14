import numpy

triangular_membership_function = {1:[1,1,1] , 2:[1,2,3] , 3:[2,3,4] , 4:[3,4,5] , 5:[4,5,6] , 6: [5,6,7] , 7:[6,7,8],8:[7,8,9],9:[9,9,9]}
test_data = [[1,5,4,7],[0.2,1,0.5,3],[0.25,2,1,3],[0.142,0.33,0.33,1]]

def main():
	#print(triangular_membership_function)
	n = len(test_data)
	fuzzified_test_data = numpy.zeros((n,n,3))

	for x in range(n):
		for y in range(n):
			if(test_data[x][y] >= 1):
				fuzzified_test_data[x][y] = triangular_membership_function[test_data[x][y]]
			else:
				index = round(1/test_data[x][y])
				#print(index)
				temp = triangular_membership_function[index]
				for i in range(3):
					fuzzified_test_data[x][y][i] = 1.0/temp[2-i]
	#print(fuzzified_test_data)

	fuzzy_geometric_mean = [[1 for x in range(3)] for y in range(n)]
	#print(fuzzy_geometric_mean)

	for i in range(n):
		for j in range(3):
			for k in range(n):
				fuzzy_geometric_mean[i][j] *= fuzzified_test_data[i][k][j]
			fuzzy_geometric_mean[i][j] = fuzzy_geometric_mean[i][j]**(1/float(n))
	#print(fuzzy_geometric_mean)

	sum_fuzzy_gm = [0 for x in range(3)]
	inv_sum_fuzzy_gm = [0 for x in range(3)]

	for i in range(3):
		for j in range(n):
			sum_fuzzy_gm[i] += fuzzy_geometric_mean[j][i]

	for i in range(3):
		inv_sum_fuzzy_gm[i] = (1.0/sum_fuzzy_gm[2-i])
	#print(sum_fuzzy_gm)

	fuzzy_weights = [[1 for x in range(3)] for y in range(n)]

	for i in range(n):
		for j in range(3):
			fuzzy_weights[i][j] = fuzzy_geometric_mean[i][j]*inv_sum_fuzzy_gm[j]
	#print(fuzzy_weights)

	weights = [0 for i in range(n)]
	normalized_weights = [0 for i in range(n)]
	sum_weights = 0

	for i in range(n):
		for j in range(3):
			weights[i] += fuzzy_weights[i][j]
		weights[i] /= 3
		sum_weights += weights[i]
	#print(weights)
	#print(sum_weights)

	for i in range(n):
		normalized_weights[i] = (1.0*weights[i])/(1.0*sum_weights)
	print(normalized_weights)

	return normalized_weights






if __name__=="__main__":
	main()
