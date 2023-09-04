from Fraction import Fraction
def main():
    fraction1 = Fraction(2,3)
    fraction2 = Fraction(2,3)
    fraction3 = Fraction(2,3)

    print(f"Fraction 1 is: {fraction1}")
    print(f"Fraction 2 is: {fraction1}")
    print(f"Fraction 3 is: {fraction1} \n")

    # Equals Operation
    print("Seeing is Fraction1 == Fraction2")
    if fraction1 == fraction2:
        print("They are the same!")
    else:
        print("They are not the same!")

    print("\n")
    # Greater than Operation
    if (fraction1>fraction2):
        print("Fraction 1 is greater than Fraction 2")
    else:
        print("Fraction 1 is NOT greater than fraction 2")






main()