class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber,scores ):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    def calculate(self):
        score = sum(self.scores)/ len(self.scores)
        grade = ""
        if (90<= score) and (score <=100) : 
            grade = "O"
        elif (80<= score) and (score <90) : 
            grade = "E"
        elif (70<= score) and (score <80) :
            grade = "A"
        elif (55<= score) and (score <70) :
            grade = "P"
        elif (40<= score) and (score <55) :
            grade = "D"
        elif score < 40 :
            grade = "T"
        return grade
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
