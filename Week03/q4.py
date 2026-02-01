monday_calss ={"Alice", "Bob", "Charlie", "Diana"}
wednesday_class ={"Bob", "Diana", "Eve", "Frank"}

monday_calss.add("Grace")
print("Monday Class ",monday_calss)
print("Wednesday Class ",wednesday_class)

bot_class= monday_calss & wednesday_class
print("Attended both classes",bot_class)

all_students = monday_calss | wednesday_class
print("Attended etheir class: ",all_students)

only_monday= monday_calss - wednesday_class
print("Onlay Monday : ",only_monday)

onlay_one = monday_calss ^ wednesday_class
print("Onlay one class : ",onlay_one)
print("Is Monday subset of all students ?",monday_calss <= all_students)