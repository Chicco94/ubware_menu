def remove_void(lst:list):
	return list(filter(None, lst))

def remove_double_back(string:str):
	string.replace("\n\n","@@@@@").replace("\n","").replace("@@@@@","")

def pretty_print(dct:dict):
	for val,key in dct.items():
		print(val)
		for el in key:
			print("\t",el)
		print("\n")