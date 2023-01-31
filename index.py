#!/usr/bin/env python3
import cgitb, random

logo_file = 'loveislandlogo.png'
cliche_file = 'cliches'
total = 25
width = 5

header = ("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>\n"
        "<html lang='en'>\n<head>\n"
        "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n"
        "<title>Love Island Cliché Bingo</title>\n"
        "<link rel='stylesheet' type='text/css' href='css/style.css'>\n"
        "</head>\n<body>\n"
        "\t<center>\n\t\t<h1>Love Island Cliché Bingo</h1>\n\t</center>")

footer = ("<br />"
        "\t</body>\n</html>")


def generate_table(ts):
    """Generates an HTML table representation of the bingo card for terms"""
    res = "<table>\n"
    count = 1
    for i, term in enumerate(ts):
        if i % width == 0:
            res += "\t<tr>\n"
        if count == (total-1)/2+1:
            res += "\t\t<td><img src='" + logo_file + "' height='100' width='100'></td>\n"
        else:
            res += "\t\t<td>" + term.strip('\n') + "</td>\n"
        if i % width == width - 1:
            res += "\t</tr>\n"
        count += 1
    res += "</table>\n"
    return res


def main():
    cgitb.enable()
    print("Content-Type: text/html;charset=utf-8\r\n\r\n")
    with open(cliche_file, encoding="utf-8") as infile:
        terms = infile.readlines()
    print(header)
    random.shuffle(terms)
    print(generate_table(terms[:total]))
    print(footer)


if __name__ == "__main__":
    main()
