from game.word import Words
import random
class Guesser: 
    
    def __init__(self):
        #self.word = Words
        self.list = ['stock', 'over', 'flow']
        self.word = random.choice(self.list)
        self._word_in_progress = []
        self.j = 0
        self.size = len(self.word)
        for self.j in self.word:
            self._word_in_progress += '_'

    def guess (self): 
        failed = 0
        self.guesser = True
        j = 0

        guess = input('Guess a letter [a-z]: ')

        for letter in self.word:
                if self._word_in_progress[j] == '_':
                    if letter == guess:
                        self._word_in_progress[j] = letter
                    #replace the j element in the line
                    else:
                        failed += 1
                else:
                    failed += 1
                j += 1
        
        if failed == self.size:
            self.guesser == False


                
        return self._word_in_progress