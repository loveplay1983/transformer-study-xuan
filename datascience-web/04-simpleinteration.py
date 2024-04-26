from taipy.gui import Gui, notify

text = "Hello, dwdadorld!"

# page
page = """
# Gettting started with taipy simple interaction!
  
Text: <|{text}|>    

<|{text}|input|>   

<|Test|button|on_action=on_button_action|> \ \ \ <|Sidebutton|button|on_change=on_change|>
"""

def on_button_action(state):
    notify(state, "info", f"The text is : {state.text}")
    state.text = "Button pressed."


def on_button_action_2(state):
    notify(state, "info", f"The text is : {state.text}")
    state.text = "Button pressed."

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return 


Gui(page).run(debug=True, use_reloader=True)

