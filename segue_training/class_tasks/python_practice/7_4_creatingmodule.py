import salarycalc as sc

E1 = sc.slarycalc("Harish", BP=25000, allowance=10000, hra=6500)
print(f"Salary of {E1.employee} :", E1.calc_salary())

E2 = sc.slarycalc("Ram", BP=76000, allowance=30000, hra=4500)
print(E2.np())
print(E2.issues())
print(f"Salary of {E2.employee} :", E2.calc_salary())

E3 = sc.slarycalc("Sita", BP=80000, allowance=40000, hra=8500)
print(f"Salary of {E3.employee} :", E3.calc_salary())
print("Salary after hike for sita :", E3.hike(40))
