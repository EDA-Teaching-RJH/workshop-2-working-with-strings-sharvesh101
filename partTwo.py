import math  

def main():
    side1 = int(input("Enter side A: "))
    side2 = int(input("Enter side B: "))
    result = pythag(side1,side2)
    print(result)

def pythag(A,B):
    C = math.sqrt(math.pow(A,2) + math.pow(B,2))
    return C

main()
