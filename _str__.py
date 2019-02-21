# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 03:41:21 2019

@author: Giga
"""

def __str__(self):
        square = 8 #size of our chessboard (the assignment example has 4x4)
        r = ''
        #r += '   '
        '''
        for i in range(square):
            r += '%d ' % (i+1)
        r += '\n  ' + '--'*square + '\n'
        '''
        
        for i in range(square,0,-1):
            #r += '%d|' % i
            for j, queen in enumerate(self.state):
                if queen == i:
                    r += ' O'
                else:
                    r += ' -'
            r += '\n'
        #r += '  ' + '--'*square + '\n'
        print(self.fitness())
        return r