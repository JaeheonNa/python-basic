from collections import OrderedDict

dic1 = {'가':1, '나':2, '다':3}
dic2 = {'가':1, '다':3, '나':2}
print(id(dic1))
print(id(dic2))
print(dic1 == dic2)

ord1 = OrderedDict({'가':1, '나':2, '다':3})
ord2 = OrderedDict({'가':1, '다':3, '나':2})
print(id(ord1))
print(id(ord2))
print(ord1 == ord2)