import pytest
from rover import *

@pytest.fixture(name='r', scope='function')
def rover_fixture():
	yield Rover()

def test_move_up(r):
	# If I have a rover
	# and I move up ('U')
	# them the rover "should move" 
	# --> rover position?
	# --> how to give commands to the rover?
	# r.move_up()  # starts at (0,0)
	r.command('U')
	assert r.position == (0,1)

def test_move_down(r):
	r.command('D')
	assert r.position == (0, -1)

	
def test_move_left(r):
	# If I have a rover
	# and I move up ('U')
	# them the rover "should move" 
	# --> rover position?
	# --> how to give commands to the rover?
	# r.move_up()  # starts at (0,0)

	r.command('L')
	assert r.position == (-1,0)

def test_move_right(r):
	r.command('R')
	assert r.position == (+1, 0)

def test_composite_command(r):
	r.command('LRR')
	assert r.position == (+1, 0)

def test_unknown_command_throws_exception(r):
	with pytest.raises(UnknownCommandException):
		r.command('@')

def test_zero_length_command(r):
	with pytest.raises(EmptyCommand):
		r.command('')




