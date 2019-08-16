def number_to_fizz_buzz(number_to_be_fizz_buzzed: int, fizz_divider: int = 3, buzz_divider: int = 5):
    fizz_buzz_divider = fizz_divider * buzz_divider

    if number_to_be_fizz_buzzed % fizz_buzz_divider == 0:
        return 'fizz buzz'
    
    if number_to_be_fizz_buzzed % fizz_divider == 0:
        return 'fizz'

    if number_to_be_fizz_buzzed % buzz_divider == 0:
        return 'buzz'

    return number_to_be_fizz_buzzed