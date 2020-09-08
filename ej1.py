"""
author: Ariel Suil Aravena [asuil]
date: 03-09-2020

a basic implementation of a Perceptron
"""


# class for a Perceptrion
class Perceptron:

	# init method
	# weight1 (float), weight2 (float), bias (float) => Perceptron
	def __init__(self, weight1, weight2, bias):
		self.__w1 = weight1
		self.__w2 = weight2
		self.__b = bias

	# evaluation method
	# x1 (int), x2 (int) => int
	def eval(self, x1, x2):
		res = x1*self.__w1 + x2*self.__w2 + self.__b
		return 1 if res > 0 else 0


# class to test Perceptron behaviour
class TestPerceptron:

	# init method (empty)
	def __init__(self):
		pass

	# test method
	# per_fun (dict(Perceptron:lambda)) => None
	# compares behaviour of Perceptron with associated lambda
	@classmethod
	def test(cls, per_fun):
		for perceptron in per_fun:
			function = per_fun[perceptron]
			for n in (0, 1):
				for m in (0, 1):
					assert perceptron.eval(n, m) == function(n, m)


if __name__ == '__main__':
	
	OR = Perceptron(1, 1, -0.5)
	AND = Perceptron(1, 1, -1.5)
	NAND = Perceptron(-1, -1, 1.5)

	TestPerceptron.test(
		{
			OR: (lambda a, b: int(a or b)),
			AND: (lambda a, b: int(a and b)),
			NAND: (lambda a, b: int(not (a and b)))
		}
	)