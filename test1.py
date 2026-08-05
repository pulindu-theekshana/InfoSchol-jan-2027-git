st_count = 1

while st_count <= 5:
    marks = int(input("Input marks: "))

    if marks >= 70:
        print("A")
        if marks == 100:
            print("Max marks")
    elif marks >= 55:
        print("B")
    elif marks >= 40:
        print("C")
    else:
        print("F")

    st_count += 1