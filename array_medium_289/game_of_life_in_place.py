class Solution:
    def count_neigbors(self, board, i, j) -> int:
        count = 0
        if i:
            if j:
                count += board[i - 1][j - 1]
            count += board[i - 1][j]
            if j < self.m - 1:
                count += board[i - 1][j + 1]
        if j:
            count += board[i][j - 1]
        if j < self.m - 1:
            count += board[i][j + 1]
        if i < self.n - 1:
            if j:
                count += board[i + 1][j - 1]
            count += board[i + 1][j]
            if j < self.m - 1:
                count += board[i + 1][j + 1]
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)
        self.m = len(board[0])
        new_line =[
            [0] * self.m,
            [0] * self.m,
        ]
        k = 0
        for i in range(self.n):
            for j in range(self.m):
                count = self.count_neigbors(board, i, j)
                if board[i][j]:
                    new_line[k][j] = 0 if count < 2 or count > 3 else 1
                else:
                    new_line[k][j] = 1 if count == 3 else 0
            if i:
                for j in range(self.m):
                    board[i - 1][j] = new_line[(k + 1) % 2][j]
            k += 1
            k %= 2
        for j in range(self.m):
            board[self.n - 1][j] = new_line[(k + 1) % 2][j]
