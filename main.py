# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('s')
queue.append('h')
queue.append('i')
queue.append('v')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from the queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty