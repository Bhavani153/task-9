#1
data=[10,501,22,37,100,999,87,351]
result=filter(lambda x: x>4, data)
print(list(result))
#In the given program, expected o/p is same as the data element. 
#In filter methord, true condition element get printed as an o/p, here the condition is x>4, all the data elements are >4 so its print data as an o/p

#2
x=[98,56,"abc",7,"apple",78,"xxx"]
#print("The given list is : " + str(x))
list_type = list(map(lambda x: "integer" if isinstance(x, int) else "string", x))
print("The types of elements in the list are:"+str(list_type))

#3
def fibonacci(count):
    fib_list=[1,1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2,count)))
    return fib_list[:count]
print("fibonacci of 1 to 50 elements:")
print(fibonacci(50))

#4)a
import re
reg_exp=re.compile(r'([a-zA-Z0-9]+[.-_])*[a-zA-Z0-9]+@[a-zA-Z0-9-]+(\.[A-Z|a-z]{2,})+')
def email_validation (email):
    if re.fullmatch(reg_exp, email):
        print("This is a valid mail")
    else:
        print("This is a Invalid mail")
email_validation("bhavanikannank@gmail.com")
email_validation("kljgdug@ymail.co.us59")
email_validation("bhavanikannan153@gmail.com")
email_validation("....@chj.us")

#b)
import re
def Mnumber_validation (mobileno):
    reg_exp=re.compile(r'(^(((\+|00)?880)|0)(\d){10}$)')
    return bool(reg_exp.match(mobileno))
mobilenos=["+91 9653763647","+8801996409999","+8801812598624","01812598624","+8801736458080","+880 1760123128"]
for mobileno in mobilenos:
    if Mnumber_validation(mobileno):
        print(f"{mobileno} is a valid mobile number")
    else:
        print(f"{mobileno} is an invalid mobile number")

#c)
import re
def Mnumber_validation (mobileno):
    reg_exp=re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    return bool(reg_exp.match(mobileno))
mobilenos=["4441234567", "123-456-6789","456-678"]
for mobileno in mobilenos:
    if Mnumber_validation(mobileno):
        print(f"{mobileno} is a valid USA number")
    else:
        print(f"{mobileno} is an invalid USA number")

#d)
import re
def verify_passwd(passwd):
    reg_exp = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16}$")
    return bool(reg_exp.match(passwd))
passwds = ['Abcd12@jgdilnvdg', 'Xyz*87','Abuihdk$76']
for passwd in passwds:
    if verify_passwd(passwd):
        print(f"{passwd} is a valid password")
    else:
        print(f"{passwd} is an invalid password")