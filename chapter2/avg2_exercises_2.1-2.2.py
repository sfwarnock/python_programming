# avg2.py
#   A simple program to average three exam scores.
#   Illustrates use of multiple input

#   User enter three exam scores, seprating each by a comma(,), then press enter.

def main():
    print("This program computes the average of three exam scores.")
    
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    avg = (score1 + score2 + score3) / 3
    print ("The average of the two scores is: ", avg)
    
main()