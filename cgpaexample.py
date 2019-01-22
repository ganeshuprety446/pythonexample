#cgpa calculator
CA_marks=int(input("enter your ca marks out of 100"))
MTE_marks=int(input("enter your mte marks out of 40"))
ETE_marks=int(input("enter your ete marks out of 70"))
ATT_marks=int(input("enter your att marks out of 5"))
print("ca marks is ",CA_marks)
print("mte marks is ",MTE_marks)
print("ete marks is ",ETE_marks)
print("att marks is ",ATT_marks)
sub1_total=CA_marks+MTE_marks+ETE_marks+ATT_marks
print("sub1 total is",sub1_total)
sub1weighted_marks=sub1_total*100/215
print("sub1 weighted is",sub1weighted_marks)
percentage=sub1weighted_marks*100/100
print("percentage is",percentage)
cgpa=percentage/10
print("cgpa is",cgpa)
