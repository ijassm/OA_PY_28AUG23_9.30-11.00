class Person:
    def __init__(self, name, age, skills=[]):
        self.name = name
        self.age = age
        self.school = "imaculate"
        self.voteEligibility = "YES" if age >= 18 else "NO"
        self.skills = skills

    def getDetails(self):
        print("-----Details-----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", self.school)
        print("VoteEligibility:", self.voteEligibility)
        print("Skills:", self.skills if self.skills else "NO SKILLS")
        print("----Details End-----\n")

    def changeSchool(self, currentSchool):
        print("school is changed for", self.name)
        print(f"{self.name} old school name is", self.school)
        self.school = currentSchool
        print(f"{self.name} current school name is", self.school)


obj1 = Person("abc", 18, ["PY", "JAVA", "C"])
obj2 = Person("xyz", 10, ["PY"])

# changing school name
obj1.changeSchool("petit")

obj1.getDetails()
obj2.getDetails()
