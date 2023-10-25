# Get input message and choose whether to code or decode
msg = input("Enter a message: ")
coding = input("Enter 1 for coding and 0 for decoding: ")
coding = True if coding == "1" else False

# Split the message into words based on spaces
words = msg.split(" ")

# Code the message or decode the coded message based on the chosen operation
if coding:
    # Code the message
    code = []
    for word in words:
        if len(word) >= 3:
            st = word[1:] + word[0]
            r_c = "nccaoiuhpun"
            st = r_c + st + r_c
            code.append(st)
        else:
            code.append(word[::-1])
    print(" ".join(code))
else:
    # Decode the coded message
    code = []
    for word in words:
        if len(word) >= 3:
            st = word[11:-11]
            st = st[-1] + st[:-1]
            code.append(st)
        else:
            code.append(word[::-1])
    print(" ".join(code))
