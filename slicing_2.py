color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
for i in range(len(color)):
    if i == 0 or i == 4 or i == 5:
        continue
    else:
        print(color[i])
