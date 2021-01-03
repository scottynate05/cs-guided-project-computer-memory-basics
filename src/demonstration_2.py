"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."

we can use a bitwise and to check the last digit of n 
and if it is a 1 then increment a counter
​
we can use bitshift to the right to move our scope 
or vison of the binary number of n 
in effect incrementing our loop
​
another option in python you can convert 
to a binary string by using the bin() function
​
.count method exists in a string
​
turn n in to a binary string
run .count('1') on the binary string
returning the result

"""
def hamming_weight(n):
    # set a counter
    counter = 0

    # iterate over n until it's equal to zero
    while n != 0:
        # check if n (bitwise and) is equal to 1
        if n & 1 == 1:
            # increment counter
            counter += 1
        # bit shift n to the right
        n = n >> 1
    
    # return counter
    return counter

def hamming_2(n):
    # set a counter
    counter = 0

    # convert n to a binary string
    binary_str = bin(n)

    # iterate over each char of the binary string
    for i in binary_str:
        # if the char is equal to 1
        if i == '1':
            # increment the counter
            counter += 1

    # return the counter
    return counter

# single line solution
def hamming_3(n):
    return bin(n).count('1')
    # convert n to a string and return the count of the char we're looking for

print(hamming_weight(10))
print(hamming_2(4))
print(hamming_3(130))