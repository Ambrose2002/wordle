import random
import pathlib
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width = 40, theme=Theme({'warning': 'red on yellow'}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")   
    
def main():
    # Pre-process
    
    WOTD = get_random_word()
    print(WOTD)
    guesses = ['_' *5] *6

    # Process (main loop)  
    # for guess_num in range(1, 7):
    #     guess = input(f"\nGuess {guess_num}: ").upper()
        
    #     if guess == WOTD:
    #         print('YOu guessed it right!')
    #         break
    #     show_guess(guess, WOTD)
    
    for idx in range(6):
        refresh_page(headline = (f'Guess {idx + 1}'))
        print(WOTD)
        show_guesses(guesses, WOTD)
        guesses[idx] = input('\nGuess word: ').upper()
        
        guesses[idx] = guess_word(previous_guesses = guesses[:idx])
        if guesses[idx] == WOTD:
            print('You\'ve got it right!')
            break

    # Post-process
    
    game_over(guesses, WOTD)
        
def get_random_word():
    WORDLIST = pathlib.Path('wordlist.txt')

    if words := [
        word.upper() 
        for word in WORDLIST.read_text(encoding = 'utf-8').split('\n')
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        console.print('No words of length 5 in the word list', style = 'warning')
        raise SystemExit()
    
def show_guesses(guesses, WOTD):
    # correct_letters = {
    # letter for letter, correct in zip(guess, WOTD) if letter == correct
    # }
    # misplaced_letters = set(guess) & set(WOTD) - correct_letters
    # wrong_letters = set(guess) - set(WOTD)
    
    # print('Correct letters:', ','.join(sorted(correct_letters)))
    # print('Misplaced letters:', ','.join(sorted(misplaced_letters)))
    # print('Wrong letters:', ','.join(sorted(wrong_letters)))
    
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, WOTD):
            if letter == correct:
                style = 'bold white on green'
            elif letter in WOTD:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'white on #666666'
            else:
                style = 'dim'
                
            styled_guess.append(f'[{style}]{letter}[/]')
            
        console.print("".join(styled_guess), justify = 'center')
        
    
def guess_word(previous_guesses):
    guess = console.input('\nGuess word: ').upper()
    
    if guess in previous_guesses:
        console.print(f'You/ve already guessed {guess}.', style = 'warning')
        return guess_word(previous_guesses)
    
    if len (guess) != 5:
            console.print(f"Your guess must be", 5, " letters.", style="warning")        
            return guess_word(previous_guesses)
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f"Invalid letter: '{invalid}'. Please use English letters.", style ='warning')
        return guess_word(previous_guesses)

    
    return guess


def game_over(guesses, WOTD):
    print(f'The word was {WOTD}')

if __name__ == '__main__':
    main()
    

            
            

                
        
