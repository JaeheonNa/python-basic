def offer(queue, data):
    queue.append(data)

def poll(queue):
    if len(queue) > 0:
        return queue.pop(0)
    else:
        print("Queue is empty.")
        return False

if __name__ == "__main__":
    queue = []
    for i in range(1, 5):
        offer(queue, i)
        print("Queue의 현재 상태:", queue)

    for i in range(1, 5):
        poll(queue)
        print("Queue의 현재 상태:", queue)
