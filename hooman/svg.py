class SVG:
    @classmethod
    def tag(
        cls, tag_name: str, content: str = "", attributes: dict = {}, self_close=False
    ) -> str:
        attribs = []
        for k in attributes:
            if attributes[k]:
                attribs.append(f'{k}="{str(attributes[k])}"')

        attribs_str = " ".join(attribs)

        if not self_close:
            return f"<{tag_name} {attribs_str}>{content}</{tag_name}>"
        else:
            return f"<{tag_name} {attribs_str}/>"

    @classmethod
    def save(cls, commands, path, width, height):
        commands_str = "\n".join(commands)
        string = f"""
<svg version="1.1"
     width="{width}" height="{height}"
     xmlns="http://www.w3.org/2000/svg">

{commands_str}

</svg>
"""

        with open(path, "w+") as f:
            f.write(string)

        if len(commands) == 0:
            print("warning! SVG mode not enabled!")
        print("saved svg to", path)
