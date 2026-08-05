St = input("Enter a message: ")
s = int(input("1 = Encode, 0 = Decode: "))

if s == 1:
    if len(St) >= 3:
        w1 = input("Enter first 3-letter string: ")
        w2 = input("Enter second 3-letter string: ")

        encoded = w1 + St[1:] + St[0] + w2
        print("Encoded:", encoded)
    else:
        print("Cannot encode")

elif s == 0:
    if len(St) >= 9:   # 3 + original + 3
        temp = St[3:-3]
        decoded = temp[-1] + temp[:-1]
        print("Decoded:", decoded)
    else:
        print("Invalid encoded message")

else:
    print("Invalid choice")