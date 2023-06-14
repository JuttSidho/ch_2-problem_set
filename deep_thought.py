"""
implement a program that prompts the user for the answer to the Great
Question of Life, the Universe and Everything, outputting Yes if the 
user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

great = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower

if great == "42":
    print("Yes")
if great == "forty-two":
    print("Yes")
if great == "forty two":
    print("Yes")
else:
    print("No")
