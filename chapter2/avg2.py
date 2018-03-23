# avg2.py
#   A simple program to average two exam scores.
#   Illustrates use of multiple input

def main():
    print("This program computes the average of two exam scores.")
    
    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    avg = (score1 + score2) / 2
    print ("The average of the two scores is: ", avg)
    
main()