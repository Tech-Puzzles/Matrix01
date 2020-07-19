import sys
import time
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
PAUSE=1

class Solution(object):
    def __init__(self):
        self.iterations=0

    def printx(self,mode,matrix,i=None,j=None,testi=None,testj=None):
            height = len(matrix)
            width = len(matrix[0])
            print('\x1b[2J')
            print(mode)
            print ("=== len(matrix): ",len(matrix))
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                        char=' '
                        ctrl=None
                        if row == i and col == j:
                            char=' >>'
                            ctrl=Fore.RED
                        if row == testi and col == testj:
                            char=' >>'
                            ctrl=Fore.YELLOW
                        if ctrl:
                            print(Style.BRIGHT+ctrl, end="")
                        else:
                            print('  ', end="")
                        print(char, end="")
                        print(Style.RESET_ALL, end="")

                        if matrix[row][col] == 0:
                            print(Fore.BLUE + '[0]', end="")
                            print(Style.RESET_ALL, end="")
                        else:
                            # matrix[row][col] == 0:
                            #print('\x1b[38;2;100;100;100mTRUECOLOR\x1b[0m',end="")
                            #scale=str(int(256*matrix[row][col]/(height+width)))

                            # scale the max down
                            scale=str(int(256*matrix[row][col]/int((height+width)/1)))
                            #print('Scale:'+ scale,end="")
                            #print('\t\x1b[30m Black foreground\x1b[0m',end="")
                            print(Back.WHITE + Style.BRIGHT + '\x1b[38;2;'+scale+';'+scale+';'+ scale+'m',end="")
                            print(f"{matrix[row][col]:3d}",end="")
                            print(Style.RESET_ALL, end="")
                print()
            if mode=='UPDATE':    
                time.sleep(PAUSE)
            elif mode.startswith('TEST'):    
                time.sleep(1)

    def check(self, isforward,matrix, height, width, i, j):
            self.iterations+=1
            # look up
            if (isforward):
                self.printx('TEST LOOK UP',matrix,i,j,i-1,j)
            if (isforward and i > 0 and matrix[i-1][j] + 1 < matrix[i][j]):
                print(i,j,'UPDATE: look up update BEFORE: ',  matrix[i][j] , 'AFTER:', matrix[i-1][j] + 1)
                matrix[i][j] = matrix[i-1][j] + 1
                self.printx('UPDATE',matrix,i,j,i-1,j)

            # look down
            if (not isforward):
                self.printx('TEST LOOK DOWN',matrix,i,j,i+1,j)
            if (not isforward and i + 1 < height and matrix[i+1][j] + 1 < matrix[i][j]):
                print(i,j,'UPDATE: look down update BEFORE: ',  matrix[i][j] , 'AFTER:', matrix[i+1][j] + 1)
                matrix[i][j] = matrix[i+1][j] + 1
                self.printx('UPDATE',matrix,i,j,i+1,j)

            # look left
            #print('TEST',i,j,'look left', j , '>0', matrix[i][j-1] +1, '<',matrix[i][j] )
            if (isforward):
                self.printx('TEST LOOK LEFT',matrix,i,j,i,j-1)
            if (isforward and j > 0 and matrix[i][j-1] + 1 < matrix[i][j]):
                print(i,j,'UPDATE: look left update BEFORE: ',  matrix[i][j] , 'AFTER:', matrix[i][j-1] + 1)
                matrix[i][j] = matrix[i][j-1] + 1
                self.printx('UPDATE',matrix,i,j,i,j-1)

            # look right
            if (not isforward):
                self.printx('TEST LOOK RIGHT',matrix,i,j,i,j+1)
            if (not isforward and j + 1 < width and matrix[i][j+1] + 1 < matrix[i][j]):
                print(i,j,'UPDATE: look right update BEFORE: ',  matrix[i][j] , 'AFTER:', matrix[i][j+1] + 1)
                matrix[i][j] = matrix[i][j+1] + 1
                self.printx('UPDATE',matrix,i,j,i,j+1)
    
    def updateMatrix(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[List[int]]
            """
            height = len(matrix)
            width = len(matrix[0])
            self.printx('INPUT',matrix)
            print('press enter to continue')
            input()
            for i in range(height):
                for j in range(width):
                    if matrix[i][j] != 0:
                        matrix[i][j] = height + width
            self.printx('ALL',matrix)
            print('press enter to continue')
            input()
                    
            # traverse forward
            print('traverse forward')
            for i in range(height):
                for j in range(width):
                   if matrix[i][j] == 0:
                       continue
                   self.check(True,matrix, height, width, i, j)
                
            # traverse backward
            print('traverse backward')
            for i in range(height - 1, -1, -1):
                for j in range(width -1, -1, -1):
                    if matrix[i][j] == 0:
                        continue
                    self.check(False,matrix, height, width, i, j)
            print('iterations',self.iterations)    
            self.printx('ALL',matrix)
            return matrix
if len(sys.argv) > 1:
    PAUSE=int(sys.argv[1])
test=Solution()
# print(test.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
# print(test.updateMatrix([[0,1,0],[0,1,0],[1,1,1]]))
# print(test.updateMatrix([[1,1,1],[0,1,0],[1,1,1]]))
# print(test.updateMatrix([[1,1,1],[0,1,0],[0,1,1]]))
# print(test.updateMatrix([[1,0,1],[0,0,0],[1,1,1]]))
# print(test.updateMatrix([[1,0,1],[1,1,1],[1,1,1]]))
# print(test.updateMatrix([[1,1,1,1],[1,1,0,1],[1,1,1,1]]))
print(test.updateMatrix([[0,1,1,1], \
             [1,1,1,1], \
             [1,1,1,1]]))
print(test.updateMatrix([[1,1,1,1], \
             [1,1,1,1], \
             [1,1,1,0]]))
print(test.updateMatrix([[1,1,1,1,0], \
             [1,1,1,1,1], \
             [1,1,1,1,1], \
             [0,1,1,1,1], \
             [1,1,1,1,0]  \
             ]))
# print(test.updateMatrix( [[1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0],[0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0],[1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0],[0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1],[0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0],[0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1],[1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0],[1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0],[0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0],[1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0],[0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1],[0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0],[1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1],[1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0],[0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0],[0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0],[1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1],[1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0],[0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1],[0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1],[1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0],[0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1],[1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0],[1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,1,0],[0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0],[0,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1],[0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1],[1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0],[0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1],[1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1],[0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0],[1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0],[0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,1],[0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1],[1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0],[1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0],[1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1],[1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0],[0,0,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0],[0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1],[1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1],[0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1],[1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0],[1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0],[1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0],[1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1],[0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0],[0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0],[0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1],[1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1],[1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1],[0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0],[1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1],[1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1],[0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0],[0,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1],[1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1],[0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1],[0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1],[1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0],[1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1],[1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1],[0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0],[1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0],[1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0],[1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0],[0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0],[0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1],[1,0,0,1,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0],[0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1],[0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0],[1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0],[0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1],[0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0],[0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1],[1,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1],[1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0],[0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1],[0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1],[1,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],[0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,0],[0,0,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,0],[0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0],[0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0],[1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0],[1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0]]))
