import re

def main(): 
    n = 1
    while(n<=2):

        f1 = open(f"Example{n}.md", "r")
        f2 = open(f"Result{n}.html", "w+")
        pattern1 = r'^# ' # Header 1
        pattern2 = r'^## ' # Header 2
        pattern3 = r'^### ' # Header 3
        pattern4 = r"(?<!\*)\*{2}([^\*]+?)\*{2}(?!\*)" # Bold (Uses lookbehind (?<!\*) and lookahead (?!\*) to make sure it only acts when there are exactly 2 *)
        pattern5 = r"(?<!\*)\*{1}([^\*]+?)\*{1}(?!\*)" # Italic
        pattern6 = r"^1. (.*?)$" # First element on the list
        pattern7 = r"^[2-9]. (.*?)$" # Other elements on the list   
        pattern8 = r"\[(.*?)\]\((.*?)\)" # Link
        pattern9 = r"\!\[(.*?)\]\((.*?)\)" # Img
    
        lines = (f1.read()).split("\n")
        anterior_line = ""

        for line in lines:
            
            # Header 1
            replaced_line = re.sub(pattern1, "<h1>", line)
            if replaced_line != line:
                replaced_line += "</h1>"

            #Header 2
            replaced_line2 = re.sub(pattern2, "<h2>", replaced_line)
            if replaced_line2 != replaced_line:
                replaced_line2 += "</h2>"

            # Header 3
            replaced_line3 = re.sub(pattern3, "<h3>", replaced_line2)
            if replaced_line3 != replaced_line2:
                replaced_line3 += "</h3>"

            # Bold
            replaced_line4 = re.sub(pattern4, r"<b>\1</b>", replaced_line3)

            # Italic
            replaced_line5 = re.sub(pattern5, r"<i>\1</i>", replaced_line4)

            # First element on the list
            replaced_line6 = re.sub(pattern6, r"<ol>\n<li>\1</li>", replaced_line5)

            # Other elements on the list
            replaced_line7 = re.sub(pattern7, r"<li>\1</li>", replaced_line6)
        
            # Link
            replaced_line8 = re.sub(pattern8, r'<a href="\2">\1</a>', replaced_line7)
            
            # Img
            replaced_line9 = re.sub(pattern9, r'<img src="\2" alt="\1"/>', replaced_line8)
            
            if re.match(pattern7, line) == None and (re.match(pattern6, anterior_line) or re.match(pattern7, anterior_line)): # End of list case, need to add </ol> 
                f2.write("</ol>\n")
            f2.write(replaced_line9 + "\n")

            anterior_line = line

        print(f"Result{n}.html created!")
        n = n+1

main()
        
