from textnode import TextNode, TextType
import os, shutil

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    file_transfer('static/')
    print(node)


def file_transfer(source_path):
    if os.path.exists('public/'):
        shutil.rmtree('public/')
    destination = 'public/'
    source = source_path
    os.mkdir(destination)
    for file in os.listdir(source):
        cur_path = os.path.join(source, file)
        if os.path.isfile(cur_path):
            shutil.copy(
                cur_path,
                destination
            )
        else:
            file_transfer(cur_path)


main()