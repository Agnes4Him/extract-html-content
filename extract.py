from bs4 import BeautifulSoup

# EXTRACT BABYS' NAMES

html =  open("baby2008.html")
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()  
text = soup.get_text()
text = text.split()
start = text.index("Male")
start_text = text[start:]
end = text.index("Note:")
end_text = text[end:]
for item in end_text:
    if item in start_text:
        start_text.remove(item)
name_list = []
for baby in start_text[4:]:
    for element in baby:
        if element.isnumeric():
            baby = baby.replace(element, '')
    name_list.append(baby)
print(name_list)