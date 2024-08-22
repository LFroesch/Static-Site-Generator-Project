class HTMLNode:
    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return " "
        result = ""
        for key, value in self.props.items():
            result = f'{result} {key}="{value}"'
        return result
    
    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, attributes=None, **kwargs):
        super().__init__(tag, value, attributes)
        if 'children' in kwargs:
            raise ValueError("children not allowed")

    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have a value")
        if not self.tag:
            return self.value
        pairs = []
        if self.attributes:
            for key, value in self.attributes.items():
                pairs.append(f'{key}="{value}"')
        result = " ".join(pairs)
        return f"<{self.tag}{' '+ result if result else ''}>{self.value}</{self.tag}>"





