#!/usr/bin/python3.6
#File: avg2.py
#A simple program to calculate test score averages
# 2.8 Exercises: 4

def main():
    print("This program computes the average for three test scores")

    scores = input("Enter three test score separated by commas: ").split(',')
    scores = [int(i) for i in scores]
    average = (scores[0] + scores[1] + scores[2]) / 3

    print(f"The average of the scores is: {average}")

main()
