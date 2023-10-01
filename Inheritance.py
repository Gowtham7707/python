'''
simple inheritance
multilevel inheritance
multiple inheritance
hierarchical inheritance

'''
# -----------------------< simple inheritance >-------------------
# class parent():
#     def output(self):
#        print("hi this parent")
       
# class child(parent):    
#     def outputc(self):
#        print("hi this child")
  
# s=child()
# s.outputc()
# s.output()  

# -----------------------< multilevel inheritance >-------------------

# class grandparent():
#     def outputgp(self):
#        print("hi this grant parent")

# class parent(grandparent):
#     def output(self):
#        print("hi this parent")
       
# class child(parent):    
#     def outputc(self):
#        print("hi this child")
  
# s=child()
# s.outputgp()
# s.outputc()
# s.output()


# -----------------------< multiple inheritance >-------------------



# class parent():
#     def outputgp(self):
#        print("hi this grant parent")

# class mother():
#     def output(self):
#        print("hi this parent")
       
# class child(parent,mother):    
#     def outputc(self):
#        print("hi this child")
  
# s=child()
# s.outputgp()
# s.outputc()
# s.output()



# -----------------------< hierarchical inheritance >-------------------


class parent():
    def outputgp(self):
       print("hi this grant parent")

class child1(parent):
    def output(self):
       print("hi this parent")
       
class child2(parent):    
    def outputc(self):
       print("hi this child")
  
c=child1()
c2=child2()
c.outputgp()
c.output()
c2.outputgp()
c2.outputc()