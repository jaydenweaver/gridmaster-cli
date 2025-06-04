import requests

def run():
    try:
        puzzle = getPuzzle()
        print(puzzle)
    except Exception as e:
        print(f'error occurred: {e}')

def getPuzzle():
    response = requests.get('https://sudoku-api.vercel.app/api/dosuku')

    if(response.status_code != 200): 
        raise requests.HTTPError(f'request failed with status code: {response.status_code}')
    
    return response.json()['newboard']['grids'][0]['value']


if __name__ == '__main__':
    run()