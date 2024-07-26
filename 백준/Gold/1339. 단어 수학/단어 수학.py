num = int(input())
num_list = [input() for _ in range(num)]

val_dict = {}
max_length = len(max(num_list, key=len))

for word in num_list:
    for i in range(len(word)):
        letter = word[len(word) - 1 - i]

        if val_dict.get(letter):
            val_dict[letter] += 10**i
        else:
            val_dict[letter] = 10**i
        
vals = list(val_dict.values())
vals.sort(reverse=True)

res = 0
for i in range(len(vals)):
    res += vals[i] * (9 - i)

print(res)