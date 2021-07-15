class Solution:
    def flipAndInvertImage(self, image):
        """
        the pattern is if the low and the high end of the inner lists values are equal you
        switch them and once you get the low and high equal you also switch that value
        """
        for i in range(len(image)):
            low = 0
            high = len(image[i]) - 1

            while low <= high:
                if image[i][low] == image[i][high]:
                    image[i][low] = 1 - image[i][low]
                    image[i][high] = image[i][low]
                low += 1
                high -= 1
        return image