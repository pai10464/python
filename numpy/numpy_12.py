import numpy as np


def toCelsius(f):
    # f เป็นอาเรย์หนึ่งมิติเก็บอุณหภูมืในหน่วยองศาฟาเรนไฮต์
    # คืนอาเรย์หนึ่งมิติที่เก็บอุณหภูมิในหน่วยองศาเซลเซยีสทได ้จากการแปลง ี่ แต่ละอุณหภูมิใน f
    ans = np.array([])
    for e in f:
        ans = np.append(ans, (e - 32) * 5 / 9)
    return ans


def BMI(wh):
    # wh เป็นอาเรย์สองมิติขนาด n2 แทนน ้าหนัก (หน่วยเป็น กก.) และความสูง (หน่วยเป็น ซม.)
    # ของคน n คน คอลัมน์ 0 เก็บน ้าหนัก คอลัมน์ 1 เก็บความสูง [[w1,h1], [w2,h2], ...]
    # คืนอาเรย์หนึ่งมิติที่เก็บค่า body mass index ของทุกคนใน wh
    ans = np.array([])
    for w, h in wh:
        bmi = w / (h / 100)**2
        ans = np.append(ans, bmi)
    return ans


def distanceTo(p, Points):
    # p เป็นอาเรย์หนึ่งมิติขนาด 2 ชองแทนจุดหนึ่งจุ ่ ด ชอ่ ง 0 เก็บพิกัด x ชอ่ ง 1 เก็บพิกัด y
    # Points เป็นอาเรย์สองมิติขนาด n2 เก็บพิกัดของจุดจ านวน n จุด
    # คืนอาเรย์หนึ่งมิต n ชอ่ ง ที่เก็บระยะทางที่วัดจากจุด p ถึงแต่ละจุดใน Points
    ans = np.array([])
    for x, y in Points:
        d = ((p[0] - x)**2 + (p[1] - y)**2)**(1/2)
        ans = np.append(ans, d)
    return ans


exec(input().strip())
