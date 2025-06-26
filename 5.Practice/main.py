

def create_phone_number(n):
    return "({a}) {b}-{c}".format(a=''.join(map(str, n[:3])),
                                   b=''.join(map(str, n[3:6])),
                                   c=''.join(map(str, n[6:])))

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def queue_time(customers, n):
    if not customers:
        return 0
    queue = [0] * n
    print(queue)
    for customer in customers:
        print(min(queue))
        queue[queue.index(min(queue))] += customer
    print(queue)
    return max(queue)


#print(queue_time([10, 2, 3, 3], 2))  # Expected output: 10
print(queue_time([1, 2, 3, 3, 5], 3))  # Expected output: 18