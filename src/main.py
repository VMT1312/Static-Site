from textnode import TextNode

def main():
    dummy = TextNode('This is a text node', 'Bold', 'https://www.boot.dev')
    print(dummy.__repr__())

if __name__ == "__main__":
    main()