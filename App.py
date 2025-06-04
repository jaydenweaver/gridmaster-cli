import sudoku, nonagram

def run():
    while True:
        print('\nWelcome to Gridmaster.\n\n1. Solve sudoku\n2. Solve nonagram\n3. Close application\n')
        try:
            option = int(input('Please enter the number for your desired action: '))
        except ValueError as e:
            raise ValueError(f'Invalid input: {e}')
        
        if option == 1:
            sudoku.solve()     
        elif option == 2:
            nonagram.solve()
        elif option == 3:
            print('\nClosing down...')
            quit()
        else:
            raise ValueError('Invalid option. Please enter 1, 2 or 3.')



if __name__ == '__main__':
    run()