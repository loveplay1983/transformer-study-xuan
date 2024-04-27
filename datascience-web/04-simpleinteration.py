from taipy.gui import Gui, notify

text = "Hello, world!"
test_message = "Test warning message!"

# page
page = """
# Gettting started with taipy simple interaction!
  
Text: <|{text}|>    

<|{text}|input|>   

<|Test|button|on_action=on_button_action|>
"""

def on_button_action(state):
    # Calling notify object for error message and assign test_message onto it. 
    notify(state, "error", f"The text is : {state.test_message}") 
    # state.text = "Button pressed."


# def on_button_action_2(state):
#     notify(state, "info", f"The text is : {state.text}")
#     state.text = "Button pressed."

# def on_change(state, var_name, var_value):
#     if var_name == "text" and var_value == "Reset":
#         state.text = ""
#         return 


Gui(page).run(debug=True, use_reloader=True)

