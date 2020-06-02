print("ใส่ M, G1, E ตามลำดับเลยจ้า")
M = float(input("M = "))
G1 = float(input("G1 = "))
G2 = 400
E = float(input("E = "))

g2 = 10
m = 30
e = 10
g1 = 90 - (m + e)

cal_grade = []  # [[คะแนนเกรดที่ m และ e ต่างๆ, m, e]]

while m != 51:
    while e != 21:
        grade = m * (M / 60) + g1 * (G1 / 300) + g2 * (G2 / 400) + e * (E / 101)
        if m + g1 + g2 + e == 100:
            cal_grade.append([round(grade, 3), m, e])
        e += 1
        g1 = 90 - (m + e)
    e = 10
    m += 1

print(len(cal_grade))
print("คะแนนที่เป็นไปได้ทั้งหมดอยู่ใน set นี้เรย -->", cal_grade)
print()
print("สรุปกูได้คะแนนเยอะสุด", str(max(cal_grade)[0]), "คะแนน", "   โดยที่ m = " + str(max(cal_grade)[1]),
      "และ e = " + str(max(cal_grade)[2]))