def add(x, y):
	return x + y

def div(x, y):
	if abs(y) <= 0.0000001:
		raise Exception("Div by 0")
	return x / y

def add_list(ls_of_numbers):
	return sum(ls_of_numbers)


def prod_list(ls_of_numbers):
	p = 1
	for e in ls_of_numbers:
		p *= e
	return p

