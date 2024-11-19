from enum import Enum

class TextType(Enum):
    TEXT = 'Text'
    BOLD = 'Bold'
    ITALIC = 'Italic'
    CODE = 'Code'
    LINKS = 'Links'
    IMAGES = 'Images'

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node) -> bool:
        return (
            self.text_type == node.text_type
            and self.text == node.text
            and self.url == node.url
        )
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    