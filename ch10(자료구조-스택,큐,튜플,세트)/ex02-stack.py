def push(stack, data):
    stack.append(data)

def pop(stack):
    if len(stack) > 0:
        return stack.pop()
    else:
        print("스택이 비었습니다.")
        return False

def push_data(stack):
    for i in range(1, 6):
        push(stack, i)

def pop_data(stack):
    for i in range(1, 6):
        pop(stack)

if __name__ == "__main__":
    stack = []
    push_data(stack)
    pop_data(stack)
