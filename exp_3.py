#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L

A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.7}

print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)

union = {x: max(A[x], B[x]) for x in A}
print("\nUnion:", union)

intersection = {x: min(A[x], B[x]) for x in A}
print("Intersection:", intersection)

complement_A = {x: 1 - A[x] for x in A}
print("Complement of A:", complement_A)

difference = {x: min(A[x], 1 - B[x]) for x in A}
print("Difference (A - B):", difference)

R = {}
for x in A:
    for y in B:
        R[(x, y)] = min(A[x], B[y])

print("\nFuzzy Relation R (A x B):")
for k, v in R.items():
    print(k, ":", v)

C = {'y1': 0.3, 'y2': 0.9, 'y3': 0.5}

S = {}
for y in B:
    for z in C:
        S[(y, z)] = min(B[y], C[z])

print("\nFuzzy Relation S (B x C):")
for k, v in S.items():
    print(k, ":", v)

T = {}

for x in A:
    for z in C:
        values = []
        for y in B:
            values.append(min(R[(x, y)], S[(y, z)]))
        T[(x, z)] = max(values)

print("\nMax-Min Composition (T = R o S):")
for k, v in T.items():
    print(k, ":", v)
