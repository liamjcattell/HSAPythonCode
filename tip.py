# tip calculator

mealCost = float(raw_input("How much?"))
tax = mealCost * 0.06
tip = (mealCost + tax)*0.15
total= tax + tip + mealCost

# example of using tabs
##print "Meal cost is \t\t\t", mealCost
##print "Tax is \t\t\t", tax
##print "Tip is \t\t\t", tip
##print "Total is \t\t\t", total

# format strings 
print "Meal cost is \t\t\t", mealCost
print "\n\n"
print "Tax is \t\t %6.2f" % tax
print "Tip is \t\t %6.2f" % tip
print "Total is \t\t %6.2f" % total
