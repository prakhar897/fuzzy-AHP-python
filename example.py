from fuzzy_AHP import fuzzy_AHP

AHP_features_matrix = [[1,3,5,5,5,7,7],[0.33,1,2,2,2,6,6],[0.2,0.5,1,1,1,5,4],[0.2,0.5,1,1,1,5,4],[0.2,0.5,1,1,1,5,4],[0.142,0.166,0.2,0.2,0.2,1,1],[0.142,0.166,0.25,0.25,0.25,1,1]]

def main():
	weights = fuzzy_AHP(AHP_features_matrix)
	print(weights)

if __name__=="__main__":
	main()