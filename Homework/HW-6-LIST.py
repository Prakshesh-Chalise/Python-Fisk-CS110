scores = [8, 7, 7, 4, 2, 7, 8]
for i in range(len(scores)):
    if scores[i] == 7:
        scores.pop(i)
print(scores)