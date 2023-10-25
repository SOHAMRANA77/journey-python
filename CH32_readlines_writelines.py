# Reading lines from a file
# F = open("myfile.txt", "r")
# while True:
#     line = F.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break

# Reading and processing marks from a file
f = open("marks.txt", "r")
i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Math = {m1*2}")
    print(f"SS = {m2*2}")
    print(f"EG = {m3*2}")
    print("Line == ", line)

# Writing lines to a file
f = open("lines.txt", "w")
lines = ["Soham\n", "Rana\n", "Harish"]
f.writelines(lines)  # Write the lines to the file
f.close()  # Close the file
