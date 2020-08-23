from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pa, pb = 0, 0
        len_A, len_B = len(A), len(B)
        res = []
        while pa < len_A and pb < len_B:

            A0, A1, B0, B1 = A[pa][0], A[pa][1], B[pb][0], B[pb][1]
            if A0 <= B0 <= A1 <= B1:
                res.append([B0, A1])
                pa += 1
            elif B0 <= A0 <= A1 <= B1:
                res.append([A0, A1])
                pa += 1
            elif B0 <= A0 <= B1 <= A1:
                res.append([A0, B1])
                pb += 1
            elif A0 <= B0 <= B1 <= A1:
                res.append([B0, B1])
                pb += 1
            else:
                if A0 > B1:
                    pb += 1
                else:
                    pa += 1
        return res