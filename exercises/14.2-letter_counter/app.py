par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

for i in par.lower():
    if (i==" "):
        continue
    if (counts.get(i) == None):
        counts[i] = 1
    else:
        counts[i] += 1

print(counts)
