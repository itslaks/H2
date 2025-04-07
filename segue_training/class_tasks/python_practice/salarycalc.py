class slarycalc:
    def __init__(self, employee, BP, allowance, hra):
        self.employee = employee
        self.allowance = allowance
        self.BP = BP
        self.hra = hra
        self.totalsalary = 0

    def calc_salary(self):
        self.totalsalary = self.BP + self.allowance + self.hra 
        return self.totalsalary

    def hike(self, hike):
        self.totalsalary = self.calc_salary()
        self.totalsalary += (self.totalsalary * hike) / 100
        return self.totalsalary

    def issues(self):
        return f"Issues with: {self.employee}"

    def np(self):
        return f"{self.employee} is in notice period"
