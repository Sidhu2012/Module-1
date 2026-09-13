name =input(" enter your name")
gadget = input ("enter your gadget")
agent_number= 12
rating =9.5
is_active= True

print("your name",name , type (name))
print("your gadget",gadget,type(gadget))
print("your agent_number",agent_number,type(agent_number))
print ("your rating",rating,type(rating))
print("is_active", is_active,type(is_active))
ya=str(agent_number)
print("after typecasting",ya,type(ya))

var1 =name[0:3]
var2=name[-1]
var3=var1+var2
print("secret code",var3)