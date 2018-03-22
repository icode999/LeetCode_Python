# Get all combinations of fixed size


from collections import defaultdict

class AndroidPattern(object):
    def __init__(self, listr):
        self.mapr = defaultdict(list)
        for st, en in listr:
            self.mapr[st].append(en)
            self.mapr[en].append(st)

        print self.mapr


    def getPattern(self, letter, n, visited):
        print letter, n, visited
        if n == 1:
            return [letter]

        else:
            result = list()
            visited[letter] = True
            for tletter in self.mapr[letter]:
                if not visited.has_key(tletter):
                    tresult = self.getPattern(tletter, n-1, visited)
                    for tres in tresult:
                        result.append(letter + tres)
            visited.pop(letter)

            return result



vertices = [('A', 'B'), ('A', 'D'), ('A', 'E'),
            ('B', 'D'), ('B', 'E'), ('B', 'F'), ('B', 'C'),
            ('C', 'E'), ('C', 'F'),
            ('D', 'E'), ('D', 'G'), ('D', 'H'),
            ('E', 'F'), ('E', 'H'), ('E', 'I'),('E', 'G'),
            ('F', 'H'), ('F', 'I'),
            ('G', 'H'),
            ('H', 'I')
            ]

ap = AndroidPattern(vertices)
print ap.getPattern('A', 3, {})
