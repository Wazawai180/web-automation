import requests
from bs4 import BeautifulSoup

def get_secret_content(url):
    content = requests.get(url)
    content.raise_for_status()
    return content.text

def extract_secret_message(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')

    grid = {}
    max_x = 0
    max_y = 0
    for table in tables:
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) == 3:
                char = cells[1].text.strip()
                x = int(cells[0].text.strip())
                y = int(cells[2].text.strip())
                grid[(x, y)] = char
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    return grid, max_x, max_y

def print_secret_message(grid, max_x, max_y):
    for y in range(max_y, -1, -1):
        for x in range(max_x + 1):
            char = grid.get((x, y), ' ')
            print(char, end='')
        print()

def main(url):
    html_content = get_secret_content(url)
    grid, max_x, max_y = extract_secret_message(html_content)
    print_secret_message(grid, max_x, max_y)

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    main(url)