class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            flipped = row[::-1]
            for j in range(len(flipped)):
                num = flipped[j]
                if num == 1:
                    flipped[j] = 0
                else:
                    flipped[j] = 1
            res.append(flipped)
        return res