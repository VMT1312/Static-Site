import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        line = line.lstrip()
        if len(line) > 2:
            if line[0] == '#' and line[1] == ' ':
                return line[2:].strip() 
    raise Exception('No h1 header found in this markdown')


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(os.path.join(from_path, 'index.md'), encoding='utf-8') as f:
        md = f.read()
    with open(os.path.join(template_path, 'template.html'), encoding='utf-8') as f:
        template = f.read()
    parent_node = markdown_to_html_node(md)
    html_string = parent_node.to_html()
    title = extract_title(md)
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html_string)
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(template)