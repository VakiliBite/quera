from bs4 import BeautifulSoup

def process(path):
    with open(path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return len(soup.find_all('a'))
    
            
            
            

    
