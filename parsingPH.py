'''

	paran_son@outlook.com
	19/11/14

	for Parsing dash, digit, ENG

	input)
		["abc","---","567","---","555","---","edf"]
	output)
		['abc', '567', '555', 'edf']
		567555
		abcedf

'''
# Dash string parse function
def funcParseDash(lst):
	lst_len = 0
	lst_len = len(lst)
	for element in range(lst_len-1,0,-1):
		if(lst[element] == "---"):
			lst.remove(lst[element])
	
	return lst

# Digit string parse function
def funcParseDigit(lst):
	lstNUM = ""
	for element in lst:
		if(element.isdigit()):
			lstNUM = lstNUM+str(element)
	
	return lstNUM

# Alphabet string parse function
def funcParseENG(lst):
	lstENG = ""
	for element in lst:
		if(element.isalpha()):
			lstENG = lstENG+str(element)

	return lstENG

# main function
if __name__ == "__main__":
	# input data
	data = ["abc","---","567","---","555","---","edf"]
	
	# data variable define
	data_removedDash = ""
	data_onlyENG = ""
	data_onlyNUM = ""
	
	# parsing
	data_removedDash = funcParseDash(data)
	print(data_removedDash)
	data_onlyNUM = funcParseDigit(data_removedDash)
	data_onlyENG = funcParseENG(data_removedDash)

	# print converted data
	print(data_removedDash)
	print(data_onlyNUM)
	print(data_onlyENG)

'''
# TEST CODE
lst = ["abc","---","567","---","555","---","edf"]
lstENG = ""
lstNUM = ""
lst_len = len(lst)
for element in range(lst_len-1,0,-1):
	if(lst[element] == "---"):
		lst.remove(lst[element])
for element in lst:
	if(element.isdigit()):
		lstNUM = lstNUM+str(element)
	elif(element.isalpha()):
		lstENG = lstENG+str(element)

print(lst)
print(lstENG)
print(lstNUM)
'''
