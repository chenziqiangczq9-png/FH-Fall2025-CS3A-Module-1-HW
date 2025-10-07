"""This fabulous program asks the user to enter their name,
and ask their favorite fruit.
"""


def main():
    """Ask the user to enter their name and print a polite greeting."""
    my_name = input("Please enter your name")
    print("Hi", my_name, "how are you?")
    """Ask the user to enter their favorite fruit."""
    fruit = input("Please enter your favorite fruit")
    print("Fabulous. My favorite fruit is", fruit, ", I like it too ! ")
    print(f"Hi {my_name}, let's have some {fruit}, next time!")


if __name__ == "__main__":
    main()

"""Please enter your nameZoe
Hi Zoe how are you?
Please enter your favorite fruitPeach
Fabulous. My favorite fruit is Peach , I like it too ! 
Hi Zoe, let's have some Peach, next time!
"""
