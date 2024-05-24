from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while len(matrix) != 0:
            result += matrix[0]
            del matrix[0]
            
            try:
                for i in range(len(matrix)):
                    result.append(matrix[i][len(matrix[i])-1])
                    del matrix[i][len(matrix[i])-1]
                    
                for j in range(len(matrix[-1])-1, -1, -1):
                    result.append(matrix[-1][j])
                del matrix[-1]
                
                for i in range(len(matrix)-1, -1, -1):
                    result.append(matrix[i][0])
                    del matrix[i][0]
            except IndexError:
                break
                        
        return result