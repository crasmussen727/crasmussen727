# Calvin Rasmussen
# UWYO COSC 1010
# Submission Date: 10/18/2024
# HW 01
# Lab Section:12
# Sources, people worked with, help given to: COSC101- lec9-Dictionaries.pptx.pdf
# This was a quick and easy HW that helped me understand dictionaries more. 
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores
# in different subjects.
#
# Student Data:
students = [
 {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.
#Solution

#part 1, calculating the average scores for each student
average_scores={}
for student in students:
    name=student["name"]
    scores=student["scores"]
    average_score=sum(scores.values())/len(scores)
    #part 2, storing the names of students in a new dictionary
    average_scores[name]=average_score
#part 3, printing names of students with an average score greater than 80
for name, avg_score in average_scores.items():
    if avg_score>80:
        print(f"{name} has a average score greater than 80")