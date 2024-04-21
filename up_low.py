def up_low(s):
   lowercase=0
   uppercase=0
   for char in s:
       if char.isupper():
           uppercase+=1
       elif char.islower():
           lowercase+=1
       else:
           pass
   print(f"Upercase are{uppercase}")
   print(f"Lowercase are{lowercase}")
up_low('Hello I am Pavithira Sivasamy')