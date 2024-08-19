with open('24.txt') as file:
    line = file.readline()

indexes = [i for i in range(len(line)) if line[i] == "T"]

i = 0
max_len = 0
while i + 101 < len(indexes):
    if max_len < indexes[i + 101] - indexes[i]:
        max_len = indexes[i + 101] - indexes[i] - 1

    i += 1

print(max_len)
