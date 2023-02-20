import re

def generateString(word):
    return f"ECR Repository ({word}) not empty"

'''
Task: Write a function to return the string between the brackets from generateString(), preferably using a regex expression

Note: "ECR Repository (", and ") not empty" are static. Only the string between the brackets are subject to change

Example:

randomString = generateString("name123")     # returns "ECR Repository (name123) not empty"

print(yourFunction(randomString))

Expected output: "name123"
'''
