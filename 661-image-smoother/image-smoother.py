class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
                
        res = []

        for i in range(len(img)):
            new_row = []
            for j in range(len(img[0])):
                now = img[i][j]
                sum = 0
                count = 0
                for x in range(3):
                    for y in range(3):
                        row = (i-1)+x
                        col = (j-1)+y
                        if 0 <= row < len(img) and 0 <= col < len(img[0]):#valid
                            sum +=  img[row][col]
                            count += 1
                #print(now,res[i][j],sum//count)
                new_row.append(sum//count)
            res.append(new_row)
        return res