list1 = [10, 20, 30]

list1_iter1 = iter(list1)
list1_iter2 = list1.__iter__()

print(list1_iter1.__next__())
print(list1_iter1.__next__())
print(list1_iter1.__next__())
print(list1_iter1.__next__()) # raise StopIteration

