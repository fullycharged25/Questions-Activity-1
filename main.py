#There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
tree1=int(input("What is the height of Jack's first tree? "))
tree2=int(input("What is the height of Jack's second tree? "))
tree3=int(input("What is the height of Jack's third tree? "))
tree4=int(input("What is the height of Jack's fourth tree? "))
tree5=int(input("What is the height of Jack's fifth tree? "))
sum_height = tree1+tree2+tree3+tree4+tree5
avg_height = sum_height/5
print(avg_height)