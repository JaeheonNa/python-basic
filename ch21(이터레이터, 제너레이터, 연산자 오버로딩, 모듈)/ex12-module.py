import copy

colors = [['red', 'green', 'blue']]
shallow_clone = colors.copy()
deep_clone = copy.deepcopy(colors)
colors[0].append('changedRed')

print("colors: ", colors)
print("shallow_clone: ", shallow_clone)
print("deep_clone: ", deep_clone)