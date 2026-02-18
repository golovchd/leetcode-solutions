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
        new_board = []
        for i in range(self.n):
            new_board.append([])
            for j in range(self.m):
                count = self.count_neigbors(board, i, j)
                if board[i][j]:
                    if count < 2 or count > 3:
                        new_board[i].append(0)
                    else:
                        new_board[i].append(1)
                elif count == 3:
                    new_board[i].append(1)
                else:
                    new_board[i].append(0)
        for i in range(self.n):
            for j in range(self.m):
                board[i][j] = new_board[i][j]
