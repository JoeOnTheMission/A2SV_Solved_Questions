class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        starts = []
        i = 0
        for j in range(len(mat[0])):
            starts.append([i,j])
        j = len(mat[0]) - 1
        for i in range(1,len(mat)):
            starts.append([i,j])

        d = defaultdict(list)
        index = 0
        for i,j in starts:
            
            while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                d[index].append([i,j])
                i += 1
                j -= 1

            index += 1

        direction = -1
        res = []
        for index in d:
            
            if direction == 1:
                direction = -1
                for i,j in d[index]:
                    res.append(mat[i][j])
            else:
                direction = 1
                for i,j in d[index][::-1]:
                    res.append(mat[i][j])
        return res