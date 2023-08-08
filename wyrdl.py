import random
from pathlib import Path
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width = 40, theme=Theme({'warning': 'red on yellow'}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")   
    
def main():
    
    
    WOTD = get_random_word()
    guesses = ['_' *5] *6

    
    
    for idx in range(6):
        refresh_page(headline = (f'Guess {idx + 1}'))
        
        show_guesses(guesses, WOTD)
        
        guesses[idx] = guess_word(previous_guesses = guesses[:idx])
        if guesses[idx] == WOTD:
            print('You\'ve got it right!')
            break

    
    
    game_over(guesses, WOTD)
        
def get_random_word():
    WORDLIST = Path('wordlist.txt').read_text(encoding= 'utf-8').split('\n')
    return random.choice([word for word in WORDLIST if len(word) == 5]).upper()
    
def show_guesses(guesses, WOTD):
    
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
    guess = input('\nGuess word: ').upper()
    
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
    
    

            
            
# guess = ['_' *5] *6
# print('\n'.join(guess))


# for i in range(6):
#     def guessing():
#         ans = input('Enter your guess: ')
        
#         if ans in guess:
#             print('you\'ve already guessed that')
#             guessing()
#         if len(ans) != 5:
#             print('Your guess must be 5 letters.')
#             guessing()
#         if any(letter not in ascii_letters for letter in ans):
#             print('Invalid letter')
#             guessing()
#         else:
#             guess[i] = ans
#             print('\n'.join(guess))
            
        

#     guessing()
    
        
                
        
