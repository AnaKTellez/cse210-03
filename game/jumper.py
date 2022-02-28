from game.Guesser import Guesser

class Jumper:
    """Updates the status of Jumper, showing the guesser how many guess they have left. 
    
    The responsibility of a Jumper is to keep track of many many guesses are left.
    
    Attributes:
        jumper (List['']): Image of jumper
        trys (int): Number of guesses the user has
    """
    

    def __init__(self):
        """Constructs a new Jumper.
        Args:
            self (Jumper): An instance of Jumper.
        """
        self._jumper = ['  ___',
        ' /___\ ',
        ' \   / ',
        '  \ / ',
        '   O  ',
        '  /|\ ',
        '  / \ ',
        '      ',
        '^^^^^^^']
        self.trys = 5
        self._guesser = Guesser()

        
    def update_jumper(self,guess):
        """Updates the Jumpers image
        
        Returns:
           self._jumper
        """
        if guess == False: 
            self._jumper.pop(0)
            self.trys -= 1
        if self.trys == 0:
            self._jumper.insert(0,'   x  ')
            for i in range(len(self._jumper)):
                print(self._jumper[i])
            print('Game Over')
            quit()
        for i in range(len(self._jumper)):
            print(self._jumper[i])
        return 

    def print_jumper(self):
        for i in range(len(self._jumper)):
            print(self._jumper[i])