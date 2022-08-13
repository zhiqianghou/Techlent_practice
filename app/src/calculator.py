class Calculator():
	def add(self, nums1, nums2):
		return nums1 + nums2

	def substract(self, nums1, nums2):
		return nums1 - nums2

	def multiply(self, nums1, nums2):
		return nums1 * nums2

	def divide(self, nums1, nums2):
		if nums2 == 0:
			return 0
		else:
			return nums1 / nums2


if __name__ == '__main__':
	calculator = Calculator()
	print(calculator.divide(1,100))

