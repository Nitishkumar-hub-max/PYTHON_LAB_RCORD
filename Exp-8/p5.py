num = [10, 20, 10, 30, 20, 10, 40, 20, 20]

freq = []
max_freq = 0
most_freq = None

print("Frequency of each element:")

for x in num:

    if x not in freq:
        f = num.count(x)

        print(x, ":", f)

        freq.append(x)

        if f > max_freq:
            max_freq = f
            most_freq = x

print("Most frequent element:", most_freq)