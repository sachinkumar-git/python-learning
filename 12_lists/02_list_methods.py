marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
marks.append(63) # This will change the original list
print(marks)
# marks.pop() # remove last element from the list 
marks.insert(0,2)
print(marks)
marks.remove(2)
print(marks)
marks.reverse()
print(marks)
marks.sort()
print(marks)
marks.pop()
print(marks)
marks.extend(extra_marks)
print(marks)
extra_marks.extend(marks)
print(extra_marks)