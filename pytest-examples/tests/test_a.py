from app import add, div, add_list, prod_list
import pytest

@pytest.fixture(name='ls_of_numbers', scope='module')
def list_of_numbers_fixture():
	print("\nBefore fixture yield")
	yield [1,2,3]
	print("\nAfter fixture yield")

def test_add_list_1(ls_of_numbers):
	assert add_list(ls_of_numbers) == 6

def test_prod_list_1(ls_of_numbers):
	assert prod_list(ls_of_numbers) == 6


def test_discovery():
	assert True

@pytest.mark.parametrize('a,b,c', [
	(1,2,3),
	(3,5,8),
	(2,2,4),
	(2,3,5),
])
def test_add_1(a,b,c):
	#print("\nRunning test_add_1 on", a, b, c, '\n')
	assert add(a, b) == c

def test_div_1():
	with pytest.raises(Exception):
		div(1, 0)
