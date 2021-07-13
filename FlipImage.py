class Solution:
    def flipAndInvertImage(self, image):
        """
        U
        flip the inner lists horizontally
        where there is a 1 change it to 0
        where there is a 0 change it to 1

        P
        loop through the outer list
        in the inner lists have a pointer on the first and last elements
        if the first and last elements are the same thats when we swap
        then move the first pointer forward and last backwards
        once it gets to the middle you still swap

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