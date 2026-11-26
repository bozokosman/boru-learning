students = [
    {"name": "Ali", "point": [50,60,70]},
    {"name": "Veli", "point": [60,70,80]},
    {"name": "Mehmet", "point": [70,80,90]},
    {"name": "Fatma", "point": [80,90,100]},
    {"name": "Ayse", "point": [40,50,60]}
]

# Her öğrencinin ortalamasını hesapla ve yeni listeye kaydet
students_avg= []
for student in students:
    students_avg.append({"name": student["name"], "point": sum(student["point"])/ len(student["point"])})
print(students_avg)

# Ortalamalara göre en yüksekten en düşüğe sırala
sequential = sorted(students_avg, key=lambda x: x["point"] ,reverse=True)
print(sequential)

# Ortalaması 70 ve üzeri olan öğrencileri listele
for student in sequential:
    if student["point"] >= 70:
        print(student)


# Ortalama hesaplama — tek satır
students_avg = [
    {"name": s["name"], "point": sum(s["point"]) / len(s["point"])}
    for s in students
]

# Filtreleme — tek satır
basarili = [s for s in sequential if s["point"] >= 70]
print(basarili)