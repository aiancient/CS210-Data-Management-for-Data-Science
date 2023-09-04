name = "Alice"
title = "President"
company = "Rutgers"
phone = "123-456-1234"
room = "Core 101"

header = """<html>
  <head>
    <title>My homepage</title>
  </head>
  <body>"""

s = """<p>Hi, I'm (NAME). I'm the (TITLE) of (COMPANY).</p>

    <p>Here are my contact details:</p>

    <ul>
      <li>Room: (ROOM)</li>
      <li>Phone: (PHONE)</li>
    </ul>"""

footer = """</body>
</html>"""

s = s.replace("(NAME)", name)
s = s.replace("(TITLE)", title)
s = s.replace("(COMPANY)", company)
s = s.replace("(ROOM)", room)
s = s.replace("(PHONE)", phone)

print(header + s + footer)
