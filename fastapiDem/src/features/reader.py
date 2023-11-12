import os.path
import markdown
import json


def open_md(filename):
    filepath = os.path.join("../pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        content_md = input_file.read()

    md_to_html = markdown.markdown(content_md)
    data = {
        'content': md_to_html
    }
    return data

def open_json(path_f, filename):
    filepath = os.path.join(path_f, filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        content = json.loads(input_file.read())
    return content