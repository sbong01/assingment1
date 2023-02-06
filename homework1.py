# Assignment1
#the author's name: saerin bong

# Problem 1

type("Rosewater")
type(0.001)
type(37)
type(False)

# Problem 2
# example of comma
print("Hello", "world")
#example of plus
print("Hello" + "world")

#answer: comma connects two words with space while plus connects two words without space.

# problem 3
# answer: int(), float(), str(), bool()
#examples

int(3.14)
float(3)
str(3.14)
bool(0)

# Problem 4
# answer: by using \n or using def
#using \n
print('Love is a bird \nshe needs to fly \nLove is a bird \nshe needs to fly \nLove is a bird \nshe needs to fly')

#using def
def function_name ():
    print('Love is a bird')
    print('she needs to fly')
    print('Love is a bird')
    print('she needs to fly')
    print('Love is a bird')
    print('she needs to fly')

function_name()


# Problem 5
flour = 2
milk = 1
egg = 4
oil = 0.4
vanilla = 0.012

cake = 2*flour + 0.5*(milk - egg + vanilla) + oil**2
print(cake)
