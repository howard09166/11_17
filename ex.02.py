table = {
    'id':['d10','d11','d12','d13','d14'],
    'dept':['AITA','CSIE','AITA','CSIE','AITA'],
    'ch':[95, 85, 96, 70, 88],
    'math': [65, 72, 83, 91, 60],
    'python': [90, 83, 75, 94, 79],
}
students = []
for i in range(5):
    student = {}
    for field in table:
        student[field] = table[field][i]
    students.append(student)

for s in students:
    s["avg"] = round((s["ch"] + s["math"] + s["python"]) / 3, 2)

for s in students:
    print(s["id"], s["dept"], s["avg"])

print("---")

stats = {
    "AITA": {"count": 0, "total": 0, "best": None},
    "CSIE": {"count": 0, "total": 0, "best": None},
}

for s in students:
    d = stats[s["dept"]]
    d["count"] = d["count"] + 1
    d["total"] = d["total"] + s["avg"]
    if d["best"] is None or s["avg"] > d["best"]["avg"]:
        d["best"] = s

for dept in stats:
    d = stats[dept]
    dept_avg = round(d["total"] / d["count"], 2)
    print(dept, "人數:", d["count"], "系平均:", dept_avg, "最高:", d["best"]["id"], d["best"]["avg"])