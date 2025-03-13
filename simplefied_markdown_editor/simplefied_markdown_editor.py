def print_help():
    """Prints available format and special commands"""
    print("Available format: plain bold italic header link inline-code ordered-list unordered-list new-line")
    #print("bold = **, italic=*, inline-code = `")
    print("Special commands: !help !done")

def format_text(formatter):
    """Format text use selected formatter."""
    #----------------------------- text style
    if formatter == "plain":
        text = input("Text: > ")
        return text
    elif formatter == "bold":
        text = input("Text: > ")
        return "**" + text + "**"
    elif formatter == "italic":
        text = input("Text: > ")
        return "*" + text + "*"
    elif formatter == "inline-code":
        text = input("Text: > ")
        return "`" + text + "`"
    elif formatter == "header":
        level = input("Level: > ")
    #----------------------------- check level
        if level.isdigit():
            level = int(level)
            if 1 <= level <= 6:
                text = input("Text: > ")
                return "#" * level + " " + text + "\n"
    #------------------------------
            else:
                print("Level range 1 to 6.")
        else:
            print("Level should be a number.")
        return ""
    #------------------------------------
    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return "[" + label + "](" + url + ")"
    elif formatter == "new-line":
        return "\n"
    elif formatter in ("ordered-list", "unordered-list"):
        return format_list(formatter)
    else:
        return ""

def format_list(formatter):
    """Format ordered or unordered lists."""
    num_rows = input("Number of rows: > ")
    #---------------check
    if num_rows.isdigit():
        num_rows = int(num_rows)
        if num_rows > 0:
            result = []
            for i in range(1, num_rows + 1): # Цей рядок використовує цикл for для ітерації по діапазону значень, визначеному функцією range(1, num_rows + 1).
                item = input(f"Row #{i}: > ")# range(), яка може бути ітератором.
                if formatter == "ordered-list":
                    result.append(str(i) + ". " + item)
                else:
                    result.append("* " + item)
            return "\n".join(result) + "\n"
        else:
            print("Number of rows should be > 0 ")
    else:
        print("Number of rows should be a number")
    return ""

# ----------------------- Main
markdown_text = ""

while True:
    formatter2 = input("Choose a formatter: > ").strip()
#---------------------------call hlp
    if formatter2 == "!help":
        print_help()
#-------------------------------------save
    elif formatter2 == "!done":
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown_text) #save to file
        print("Markdown saved to output.md (current dir)")
        break
#-----------------------------------
    elif formatter2 in ("plain", "bold", "italic", "inline-code", "header", "link", "new-line", "ordered-list", "unordered-list"):
        formatted_text = format_text(formatter2)
        markdown_text += formatted_text + "\n"
        #----------------------добавляем форм.текст к переменной markdown_text + enter
        print(markdown_text.strip())
    else:
        print("Unknown formatting type or command")
