from game.guesser import Guesser
from game.word import Words
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        Jumper (jumper): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        Guesser (guesser): The game's seeker.
        Word: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._words = Words()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Create the jumper and get the word
        Args:
            self (Director): An instance of Director.
        """
        
        self._jumper.update_jumper()
        #self._words.show_word()
        
        
    def _do_updates(self):
        """Keep track of the word and the jumper.
        Args:
            self (Director): An instance of Director.
        """
        self.word_in_progress = self._guesser.guess()
        

        

    def _do_outputs(self):
        """Provides a hint for the seeker to use.
        Args:
            self (Director): An instance of Director.
        """
        final_word = ''.join(self.word_in_progress)
        print(f'{final_word}\n')