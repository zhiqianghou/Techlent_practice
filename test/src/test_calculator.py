from app.src.calculator import Calculator

cal = Calculator()

def test_add():
	assert cal.add(100,1) == 101
	assert cal.add(200,1) == 201
