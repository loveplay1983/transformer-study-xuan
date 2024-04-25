
from taipy import Gui

text = "test"

page = """
# Getting started with simple taipy gui

Text: <|{text}|>

<|{text}|input|>


"""

Gui(page).run(debug=True, use_reloader=True)
