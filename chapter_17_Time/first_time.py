import time
from decimal import Decimal, getcontext


def calcProd():
    # Calculate the product of the first 100,000 numbers.
    getcontext().prec = 5000  # Set the precision to a suitable value
    product = Decimal(1)
    for i in range(1, 100000):
        product = product * Decimal(i)
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f"The result is {prod} digits long.")
print(f"Took {endTime - startTime:.2f} seconds to calculate.")
