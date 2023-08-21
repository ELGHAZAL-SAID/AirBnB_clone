import os


html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>AirBnB clone</title>
  </head>
  <body>
    <header></header>
    <footer>
      <p>ALX School</p>
    </footer>
  </body>
</html>
"""

folder_name = "web_static"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for i in range(0, 9):
    file_path = "web_static/"+str(i)+"-index.html"
    with open(file_path, "w") as f:
        f.write(html)

for i in range(100, 102):
    file_path = "web_static/"+str(i)+"-index.html"
    with open(file_path, "w") as f:
        f.write(html)
