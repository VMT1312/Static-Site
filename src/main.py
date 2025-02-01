from copystatic import file_transfer
from generator import generate_pages_recursive

def main():
    file_transfer('static/', 'public/')
    generate_pages_recursive('content', 'template.html', 'public')


main()