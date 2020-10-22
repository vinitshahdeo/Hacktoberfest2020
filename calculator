class grade_calculator:
   def __init__(self):
      self.__roll_number = 0
      self._Name = ""
      self.__marks_obtained = []
      self.__total_marks = 0
      self.__percentage = 0
      self.__grade = ""
      self.__result = ""
   def setgrade_calculator(self):
      self.__roll_number = int(input("Enter Roll Number: "))
      self.__Name = input("Enter Name: ")
      print("Enter 5 subjects marks: ")
      for n in range(5):
         self.__marks_obtained.append(int(input("Subject " + str(n + 1) + ": ")))
   def Total(self):
      for i in self.__marks_obtained:
         self.__total_marks += i
   def Percentage(self):
      self.__percentage = self.__total_marks / 5
   def calculateGrade(self):
      if self.__percentage >= 90:
         self.__grade = "0"
      elif self.__percentage >= 80:
         self.__grade = "A+"
      elif self.__percentage >= 70:
         self.__grade = "A"
      elif self.__percentage >= 60:
         self.__grade = "B+"
      elif self.__percentage >= 50:
         self.__grade = "B"
      elif self.__percentage >= 40:
         self.__grade = "C"
      else:
         self.__grade = "F"
   def Result(self):
      count = 0
      for x in self.__marks_obtained:
         if x >= 40:
            count += 1
      if count == 5:
         self.__result = "PASS"
      elif count >= 3:
         self.__result = "COMP."
      else:
         self.__result = "FAIL"
   def showgrade_calculator(self):
      self.Total()
      self.Percentage()
      self.calculateGrade()
      self.Result()
      print(self.__roll_number, "\t", self.__Name, "\t", self.__total_marks, "\t",          self.__percentage, "\t", self.__grade, "\t",
         self.__result)
def main():
   gc = grade_calculator()
   gc.setgrade_calculator()
   gc.showgrade_calculator()
if __name__ == "__main__":
   main()
