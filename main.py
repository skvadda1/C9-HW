class robot1:
    model = 322
    name = "Jeffrey"
    print("Hello I am Designation" , model , "or" , name , "as my designated human name.")

    def introduction1(self):
        print("Hello, I am assigned to help you.")

    def details1(self):
        print("My designation is" , self.model)
        print("My designated human name is" , self.name)


class robot2:
    model = 945
    name = "John"
    print("Hello I am Designation" , model , "or" , name , "as my designated human name.")

    def introduction2(self):
        print("Hello, I am assigned to help you.")

    def details2(self):
        print("my designation is" , self.model)
        print("my designated human name is" , self.name)

ob = robot1()
ob.introduction1()
ob.details1()
ob = robot2()
ob.introduction2()
ob.details2()


