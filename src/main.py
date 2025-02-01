from copystatic import file_transfer
from generator import generate_page

def main():
    file_transfer('static/', 'public/')
    generate_page('content/', '.', 'public/index.html')


main()