class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
  
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        attributes = [f'{key}={value}' for key, value in self.props.items()]
        return ' ' + ' '.join(attributes)

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
   
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props, children=None)
       
    def to_html(self):
        if self.value is None:
            raise ValueError("Value is mandatory")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
   
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
   
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props, value=None)
  
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None or self.children == []:
            raise ValueError("Children(s) is required")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"