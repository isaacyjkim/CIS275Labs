def main():
    string = input("Enter a string: ")
    count_vowels(string)

def count_vowels(string):
    vowels = [0,0,0,0,0]
    alpha = ["A","E","I","O","U"]
    count = 0
    string.lower()
    for s in string:
        if (s=='a'):
            vowels[0] += 1
        elif (s=='e'):
            vowels[1] += 1
        elif (s=='i'):
            vowels[2] += 1
        elif (s=='o'):
            vowels[3] += 1
        elif (s=='u'):
            vowels[4] += 1
    print("Your string contains the following vowels: ")
    for n in vowels:
        print(alpha[count] + ": "+str(n))
        count+=1






main()