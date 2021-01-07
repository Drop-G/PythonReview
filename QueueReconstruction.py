# based on height reconstruct the line ([a=height, b=number of people the person can see in front of them]) Hint: The individual person cannot see people who are short than them

class Solution:
    def reconstructQueue(self, input):
        input.sort(key=lambda x:
                    (-x[0], x[1])
                    )
        res = []
        for person in input:
            res.insert(person[1], person)
        return res

input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(input))
# [[5,0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
