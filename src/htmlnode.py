class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        children: {self.children}
        props: {self.props}
        """

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f"{key}: {value}" for key, value in self.props.items()])

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        """

    def to_html(self):
        html_string=""
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag:
            html_string = "<" + f"{self.tag}"
            if self.props:
                html_string += f" {self.props_to_html()}"
            html_string += f">{self.value}</{self.tag}>"
            return html_string

        return self.value


class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props = None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"""
        tag: {self.tag}
        children: {self.children}
        props: {self.props}
        """

    def to_html(self):
        html_string=""
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        for child in self.children:
            if child.children is None:
                node = LeafNode(child.tag, child.value, child.props)
            else:
                node = ParentNode(child.tag, child.value, child.children, child.props)
            html_string += node.to_html()

        return f"<{self.tag}>{html_string}</{self.tag}>"
