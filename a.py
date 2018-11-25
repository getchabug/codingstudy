a = [1,2,3,4,5,6,7,8]

for i in range(0, len(a)):
	print(a[i])

	if i == 3:
		print("This value is %d" %i)

	elif (i == 1) and (i==2):
		print("this operation is ''and''")

	elif(i==3) or (i==4):
		print("this operation is ''or''")

	else:
		continue