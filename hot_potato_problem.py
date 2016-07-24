import pythonds

def hot_potato(name_list, num):
    q = pythonds.Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
            print(q.items)
        q.dequeue()

    return q.dequeue()

print(hot_potato(['tushar','vikas','tewatia','pankay','prince'],10))

