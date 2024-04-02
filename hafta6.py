# class Person:
#     pass #bu bir yer tutucudur. Sınıfı boş bırakmak istediğimizde kullanırız.

# p1=Person()
# print(p1)
# print(type(p1))



# class Person:
#     pass #bu bir yer tutucudur. Sınıfı boş bırakmak istediğimizde kullanırız.

#     def ___init___(self ,name ,year):
#         self.name=name
#         self.year=year
#         print('init metodu çalıştı')

# p1=Person('ali',1990)
# p2=Person('veli',1995)
# p3=Person('ahmet',2000)
# print(p1)
# print(p2)
# print(p3)
# print(f'adı: {p1.name} yılı: {p1.year}')
# print(f'adı: {p2.name} yılı: {p2.year}')
# print(f'adı: {p3.name} yılı: {p3.year}')

# print(type(p1))
# print(type(p2))
# print(type(p3))









# #türetilen sınıfta çalışacak olan kod => instannce metot   => sabit bir değer değil 

# # instannce metot nedir => SINAV





# class Person:
#     # class attributes
#     address='no information about Person'
#     # constructor (yapıcı metod)
#     def __init__(self, name, year):  # kullanıcının ekleyeceği attributesler
            
#         # object attributes
#         self.name=name
#         self.year=year
#         print('init mesajı çalıştı')
        
#         # methods
    
# # instance = (object)
# p1=Person(name='ali',year=2005)
# p2=Person(name='veli',year=2012)

# print(f'name : {p1.name} year : {p1.year} address: {p1.address}')
# print(f'name : {p2.name} year : {p2.year} address: {p2.address}')

# # print(type(p1))
# # print(type(p2))





# class Person:
#     # class attributes
#     address='no information about Person'
#     # constructor (yapıcı metod)
       
    
#     def __init__(self, name, year):  # kullanıcının ekleyeceği attributesler
            
#         # object attributes
#         self.name=name
#         self.year=year
#         print('init mesajı çalıştı')
        
#         # methods
#     def intro(self):
#         print('Hello There. I am + '+self.name)


#     def calculateAge(self):
#         return 2024-self.year

    
# # instance = (object)
# p1=Person(name='ali',year=2005)
# p2=Person(name='veli',year=2012)

# print(f'adım: {p1.name} ve Yaşım: {p1.calculateAge()}')
# print(f'adım {p2.name} ve Yaşım: {p2.calculateAge()}' )




# class Circle:
#     pi=3.14
#     def ___init___(self,yaricap=1):
#         self.yaricap=yaricap

#     def cevre_hesapla(self):
#         return 2*self.pi*self.yaricap
    
#     def alan_hesapla(self):
#         return self.pi*(self.yaricap**2)
    

# c1=Circle()
# c2=Circle(5)

# print(f'c1: alan: {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()}')
# print(f'c2: alan: {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()}')
    




# class Person:
#     def ___init___(self):
#         print('Person classı init fonksiyonu')

# class Student(Person):
#     def ___init___(self):
#         Person.___init___(self)
#         print('Student classı init fonksiyonu')


# p1=Person()
# s1=Student()




# class Person():
#     def ___init___(self,fname,lname):
#         self.firstName=fname
#         self.lastName=lname
#         print('Person Created')
    
#     def who_am_i(self):
#         print('I am a person')
        
#     def eat(self):
#         print('I am eatting')


# class Student(Person):
#     def ___init___(self,fname,lname):
#         Person.___init___(self, fname,lname)
#         print('Student Created')
        
#     # Override
#     def who_am_i(self):
#         print('I am a student')



# p1=Person('Ali','Kara')
# s1=Student('Veli', 'Beyaz')

# print(p1.firstName + ' ' +p1.lastName)
# print(s1.firstName + ' ' +s1.lastName)

# p1.who_am_i()
# s1.who_am_i()
# p1.eat()
# s1.eat()





# class Person():
#     def ___init___(self,fname,lname):
#         self.firstName=fname
#         self.lastName=lname
#         print('Person Created')
    
#     def who_am_i(self):
#         print('I am a person')
        
#     def eat(self):
#         print('I am eatting')


# class Student(Person):
#     def ___init___(self,fname,lname,number):
#         Person.___init___(self, fname,lname)
#         self.studentnumber=number
#         print('Student Created')
        
#     # Override
#     def who_am_i(self):
#         print('I am a student')

#     def sayHello(self):
#         print('HELLO , I am a student')



# p1=Person('Ali','Kara')
# s1=Student('Veli', 'Beyaz',12398)

# print(p1.firstName + ' ' +p1.lastName)
# print(s1.firstName + ' ' +s1.lastName+ ' '+str(s1.studentnumber))

# p1.who_am_i()
# s1.who_am_i()
# p1.eat()
# s1.eat()
# s1.sayHello()





# class Person():
#     def ___init___(self,fname,lname):
#         self.firstName=fname
#         self.lastName=lname
#         print('Person Created')
    
#     def who_am_i(self):
#         print('I am a person')
        
#     def eat(self):
#         print('I am eatting')


# class Student(Person):
#     def ___init___(self,fname,lname,number):
#         Person.___init___(self, fname,lname)
#         self.studentnumber=number
#         print('Student Created')
        
#     # Override
#     def who_am_i(self):
#         print('I am a student')

#     def sayHello(self):
#         print('HELLO , I am a student')


# class Teacher(Person):
#     def ___init___(self,fname,lname,branch):
#         super().___init___(fname,lname)
#         self.branch = branch
#         print('Teacher Created')
        
#     def who_am_i(self):
#        print(f'I am a {self.branch} teacher')
        
        
# p1=Person('Ali','Kara')
# s1=Student('Veli', 'Beyaz',1234)
# t1=Teacher('Sedat', 'Metlek','Bilgisayar')

# print(p1.firstName + ' ' +p1.lastName)
# print(s1.firstName + ' ' +s1.lastName+' '+str(s1.studentnumber))

# p1.who_am_i()
# s1.who_am_i()
# t1.who_am_i()
# p1.eat()
# s1.eat()
# s1.sayHello()




# built in metot daha önceden oluşturulmuş metotlar

# super() => miras aldığımız sınıfın metotlarını kullanmak için kullanılır.


# liste string önceden tanımlanmış clsaslardır built in dir







# myList=[1,2,3]      # build in class
# myString='Kelime'   # build in class

# print(len(myList))
# print(len(myString))

# class Movie():
#     def ___init___(self, title, director, duration): 
#        self.title=title
#        self.director=director
#        self.duration=duration
#        print('movie objesi oluşturuldu')
       
#     def __str__(self):
#         return f'{self.title} by {self.director}'
    
#     def __len__(self):
#         return self.duration
    
#     def __del__(self):
#         print('Film objesi silindi')
    

# m=Movie('film adı','yönetmen adı',120)

# print(str(myList))
# print(str(m))


# print(len(myList))
# print(len(m))

# del m






# class Question:
#     def __init__(self,text,choices,answer):
#         self.text=text
#         self.choices=choices
#         self.answer=answer
    
#     def checkAnswer(self,answer):
#         return self.answer==answer
    

# # print(q1.checkAnswer('python'))
# # print(q2.checkAnswer('C#'))
# # print(q3.checkAnswer('python'))

# # Quiz
# class Quiz:
#     def __init__(self,questions):
#         self.questions=questions
#         self.score=0
#         self.questionIndex=0
    
#     def getQuestion(self):
#         return self.questions[self.questionIndex]
    
#     def displayQuestion(self):
#         question=self.getQuestion()
#         print(f'Soru {self.questionIndex+1} : {question.text}')
        
#         for q in question.choices:
#             print('-'+q)
#         answer=input('cevap: ')
#         self.guess(answer)
#         self.loadQuestion()
        
#     def guess(self, answer):
#         question=self.getQuestion()
        
#         if question.checkAnswer(answer):
#             self.score+=1
#         self.questionIndex+=1
      
        
    
#     def loadQuestion(self):  
#         if len(self.questions)==self.questionIndex:
#             self.showScore()
#         else:
#             self.displayProgress()
#             self.displayQuestion()
#     def showScore(self):
#         self.displayProgress();
#         print ('score: ', self.score)
    
#     def displayProgress(self):
#         totalQuestion=len(self.questions);
#         questionNumber= self.questionIndex+1
        
#         if questionNumber > totalQuestion:
#             print('Quiz Bitti')
#         else:
#             print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

            
            
        
        
# q1=Question('En iyi programlama dili hangisidir ?',['C#','python','javascript','java'],'python')
# q2=Question('En popüler programlama dili hangisidir ?',['python','javascript','C#','java'],'python')
# q3=Question('En çok kazandıran programlama dili hangisidir ?',['C#','javascript','java','python'],'python')
# questions=[q1,q2,q3]

# quiz=Quiz(questions)
# #quiz.displayQuestion()
# quiz.loadQuestion()



