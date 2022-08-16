from app.src.calculator import Calculator

cal = Calculator()

def test_add():
	assert cal.add(100,1) == 101
	assert cal.add(200,1) == 201

def test_subtract():
	assert cal.subtract(3, 1) == 2
	assert cal.subtract(5, 2) == 3
	assert cal.subtract(2,1) == 1
