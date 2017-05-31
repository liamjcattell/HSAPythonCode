# Program to assign letter grade accodring to the scheme
# 90 <= score <= 100    "A"
# 80 <= score <= 90     "B"
# 70 <= score <= 80     "C"
# 60 <= score <= 70     "D"
# score < 60            "F"
from math import floor

score = float(input("Please enter your score: "))
score = 65+(100-score)/10.01
print "Your score is a(n) %c" % floor(score)
