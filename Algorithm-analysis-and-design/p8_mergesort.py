import time

class SortAndCount_Merge:

    def __init__(self):
        self.A = [];

    def MergeAndCount(self, L, R):
        RC, i, j, k = 0, 0, 0, 0
        a = []
        while i < int(len(L)) and j < int(len(R)) and k < int(len(L) + len(R)):
            if L[i] > R[j]:
                a.append(R[j])
                RC += int(len(L))-i
                j += 1
            else:
                a.append(L[i])
                i += 1

        # append the rest of numbers
        if i == int(len(L)):
            a += R[j:]
        elif j == int(len(R)):
            a += L[i:]

        return (RC, a)

    def SortAndCount(self, A):
        m = int(len(A)/2)
        if m < 1:
            return (0, A)
        L, R = A[:m], A[m:]
        RCL, L = self.SortAndCount(L)
        RCR, R = self.SortAndCount(R)
        cnt, a = self.MergeAndCount(L, R)
        cnt += RCL + RCR
        return (cnt, a)

def ReadData(filename):
    with open(filename) as f:
            A = [int(p) for p in f.readlines()]
    return A

def PrintResult(t, cnt):
    print('* compute Merge version in ', t, 'seconds: ', cnt, 'inversions')

if __name__ == '__main__':
    filename = 'Q8.txt'
    A = ReadData(filename)

    t, SM = time.time(), SortAndCount_Merge()
    cnt, sortedA = SM.SortAndCount(A)
    PrintResult(time.time()-t, cnt)
