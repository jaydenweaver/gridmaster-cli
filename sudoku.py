import requests
from colorama import Fore, Style, init

init()

def solve():
    try:
        puzzle = getPuzzle()
    except Exception as e:
        print(f'error occurred: {e}')

    print('\nFetched sudoku:')
    printSudoku(puzzle)

def getPuzzle():
    response = requests.get('https://sudoku-api.vercel.app/api/dosuku')

    if response.status_code != 200: 
        raise requests.HTTPError(f'request failed with status code: {response.status_code}')
    
    return response.json()['newboard']['grids'][0]['value']

def printSudoku(puzzle):
    for i in range(9):
        row = ''
        for j in range(9):
            val = puzzle[i][j]
            if val == 0:
                cell = Fore.LIGHTBLACK_EX + '.' + Style.RESET_ALL
            else:
                cell = Fore.BLUE + str(val) + Style.RESET_ALL
            
            row += f' {cell}'

            if (j + 1) % 3 == 0 and j != 8:
                row += Fore.WHITE + ' |' + Style.RESET_ALL
        print(row.strip())

        if (i + 1) % 3 == 0 and i != 8:
            print(Fore.WHITE + '-' * 21 + Style.RESET_ALL)
