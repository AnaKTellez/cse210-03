import random
class Guesser: 
    """A person who guess the letter. 
    
    The responsibility of a Guesser is to receive the input letter and compare it with the 
    random secrer word.
    Attributes:
        list (list): List of random words.
        word (str): secret word 
        _word_in_progress (list): Guessed letters 
        j (int): loop index
        size (int) = lenght of word
    """
    
    def __init__(self):
        """Constructs a new Guesser.
        
        Args:
            self (Guesser): an instance of Guesser.
        """
        
        self.list = ['stock', 'over', 'flow', 'random', 'hello', 'computer', 'happy', 'python', 'health', 'funny']
        self.word = random.choice(self.list)
        self._word_in_progress = []
        self.j = 0
        self.size = len(self.word)

        for self.j in self.word:
            self._word_in_progress += '_'

    def guess (self): 
        """Gets the guess from the player and compare it with the secret word.
        Args:
            self (Guesser): An instance of Guesser.
        
        Returns:
            list: word in progress.
        """
        self.guesser = False

        guess = input('Enter a letter [a-z]: ')

        for idx, character in enumerate(self.word):
            if character == guess:
                self._word_in_progress[idx] = guess
                self.guesser = True
                break

        return self._word_in_progress 