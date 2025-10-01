import time

first_name = "Ru"
last_name = "Na"
full_name = first_name + " " + last_name
print(full_name)

temp = "Person " + str(100)
print(temp)

price = int("1234")
print(type(price))

price = float("1234.5")
print(type(price))

arrow = "->" * 10
print(arrow)

arrow = "->"
print(arrow * 10)

message = "My name is %s"
print(message % "Ru")

message = "Price is $%s"
print(message % 1000)

message = "It's %s-%s-%s %s:%s:%s"
now = time.localtime()
print(message % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))