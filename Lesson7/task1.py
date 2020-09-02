class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


    def __add__(self,other):
        m_0 = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        
        for i in range(len(self.matrix)):

            for j in range(len(self.matrix)):
                m_0[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m_0]))


m_1= Matrix([[1, 1, 1],[2, 2, 2],[3, 3, 3]])
m_2= Matrix([[4, 4, 4],[2, 2, 2],[3, 3, 3]])

print(f'{m_1}\n')
print(f'{m_2}\n')

print(m_1 + m_2)

