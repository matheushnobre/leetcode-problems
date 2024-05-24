from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def verify(group: List[str]):
            valid_elements = []
            for element in group:
                if element.isalnum():
                    valid_elements.append(element)
            return True if len(valid_elements) == len(set(valid_elements)) else False    
                    
        # 1º passo: verificar linhas
        for line in board:
            if verify(line) == False:
                return False
            
        # 2º passo: verificar colunas
        for j in range(9):
            collum = [board[i][j] for i in range(9)]
            if verify(collum) == False:
                return False
        
        # 3º passo: verificar submatrizes
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                submatriz = [board[i][j] for i in range(m, m+3) for j in range(n, n+3)]
                if verify(submatriz) == False:
                    return False
        
        return True