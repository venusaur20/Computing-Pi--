import math

def pie(accuracy):
    positive = sum([
        4 / n
        for n in range(1,accuracy,4)
    ])
    negative = sum([
        4 / n
        for n in range(-3,-accuracy,-4)
    ])
    pie_number = positive + negative
    return pie_number


accuracy = int(input("Your preferred accuracy: "))
accuracy **= 4
print(pie(accuracy))