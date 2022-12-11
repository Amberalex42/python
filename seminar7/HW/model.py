def get_dict_from_base(path):
    with open(path, "r", encoding="utf-8") as file:
        line = file.readline().strip()
        database = {k: v.split(",") for k, v in [el.split(":") for el in line.split(";")]}
    return database


def set_dict_to_base(path, str_dict):
    with open(path, "w", encoding="utf-8") as file:
        file.write(str_dict)


def xml_generator(data):
    xml = '<xml>\n'
    for k, v in data.items():
        xml += "<unit>\n"
        xml += f"<name>{k}</name>\n<phone>{', '.join(v)}</phone>\n"
        xml += "</unit>\n"
    xml += '</xml>'
    with open("data.xml", "w", encoding="utf-8") as file:
        file.write(xml)


def html_generator(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for k, v in data.items():
        html += f'    <p {style}><strong>{k}</strong>: {", ".join(v)}</p>\n'
    html += '  </body>\n</html>'

    with open('index.html', 'w', encoding='utf-8') as page:
        page.write(html)
