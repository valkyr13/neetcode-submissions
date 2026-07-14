class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        4 1 0 7
        6 9 10 3
        2 2 1  1

        3 4.5 10 3

        7 4 1 0
        3 6 9 10
        1 2 2 1
        3 3 4.5 9


        """

        pair = [(position[i],speed[i]) for i in range(len(position))]
        pair.sort(reverse=True)
        print(pair)

        n = len(position)

        time = [-1]*n

        for i in range(n):
            time[i] = (target-pair[i][0])/pair[i][1]

        stack = []
        t = -1

        for i in range(n):
            if time[i] > t:
                stack.append(time[i])
                t = time[i]
            else:
                continue
        return len(stack)
        



        

        