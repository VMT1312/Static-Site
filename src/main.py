from textnode import TextNode, TextType
from copystatic import file_transfer

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    file_transfer('static/', 'public/')
    print(node)



main()