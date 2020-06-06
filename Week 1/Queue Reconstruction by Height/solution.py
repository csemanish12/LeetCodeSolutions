def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    #people.sort(reverse=True)
    people.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    queue = []
    for i in range(len(people)):
        queue.insert(people[i][1], people[i])
    return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))