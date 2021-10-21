from math import sqrt
from math import factorial
from math import floor
from math import ceil

print("Welcome to BetterCalc beta_161021_1620! See all changes in \"changelog\"")

while True:
	what = input("Operation: (+, -, *, /, ** (expanation), % (mod), // (div), sqrt (√), x! (factorial), rnd (round the number)): ")

	a = float( input("First number: ") )
	b = float( input("Second number: ") )

	if what == "+":
	    c = a + b
	    print("Result:" + str(c))
	elif what == "-":
	    c = a - b
	    print("Result:" + str(c))
	elif what == "*":
	    c = a * b
	    print("Result: " + str(c))
	elif what == "/":
	    c = a / b
	    print("Result: " + str(c))
	elif what == "**":
	    c = a ** b
	    print("Result: " + str(c))
	elif what == "%":
	    c = a % b
	    print("Result: " + str(c))
	elif what == "//":
	    c = a // b
	    print("Result: " + str(c))
	elif what == "sqrt":
		c = sqrt(a)
		print("Result: " + str(c))
	elif what == "x!":
		c = factorial(a)
		print("Result: " + str(c))
	elif what == "rnd":
		rnd = input("Round the number to \"floor\" or \"ceil\"?: ")
		if rnd == "floor":
			c = floor(a)
			print("Result: " + str(c))
		elif rnd == "ceil":
			c = ceil(a)
			print("Result: " + str(c))
	else:
	    print("Operation's inccorect")