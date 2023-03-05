A_min = int(input())
B_max = int(input())
H = int(input())
if H >= A_min and H <= B_max:
    print("Normal")
if H > B_max:
    print("Excess")
if H < A_min:
    print("Deficiency")


