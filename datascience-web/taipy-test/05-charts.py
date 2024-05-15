import pandas as pd
import plotly.graph_objects as go
from taipy.gui import Gui

# list_to_display = [100/x for x in range(1, 100)]
# fig = go.Figure(data = go.Scatter(y=list_to_display))

# page = """
# # Simple plotly graph by taipy

# Text: <|Text|input|>     
# Button: <|Test|button|on_action=on_button_action|>    
# <|chart|figure={fig}|>   
# """

# def on_button_action():
#     pass

###############################################################################
# data = {
#     "x-col": [0, 1, 2],
#     "y-col": [4, 1, 2]
# }

# page = """
# # Test 
# <|{data}|chart|x=x-col|y=y-col|>
# """

###############################################################################
# data = {
#     "x_col": [0, 1, 2], 
#     "y_col_1": [4, 2, 1], "y_col_2": [3, 1, 2]
# }

# page = """
# <|{data}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|>

# """

###############################################################################


# data = {"x_col": [0, 1, 2], 
#         "y_col_1": [4, 2, 1], 
#         "y_col_2":[3, 1, 2]}

# page = """
# <|{data}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|color[1]=green|color[2]=white|>

# """
###############################################################################

# data = {"x_col": [0, 1, 2], "y_col_1": [4, 1, 2], "y_col_2": [3, 1, 2]}

# html = """
# <|{data}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|type[1]=bar|>

# """


###############################################################################

dataframe = pd.DataFrame(
    {
        "Text":['Test', 'Other', 'Love'],
        "Score Pos":[1, 1, 4],
        "Score Neu":[2, 3, 1],
        "Score Neg":[1, 2, 0],
        "Overall":[0, -1, 4]
    }
)

# page = """
# # Test
# <|{dataframe}|table|>
# <|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
# """

property_chart = {"type": "bar",
                  "x": "Text",
                  "y[1]": "Score Pos",
                  "y[2]": "Score Neu",
                  "y[3]": "Score Neg",
                  "y[4]": "Overall",
                  "color[1]": "green",
                  "color[2]": "grey",
                  "color[3]": "red",
                  "type[4]": "line"
                }

page = """
<|{dataframe}|table|>
<|{dataframe}|chart|properties={property_chart}|>
...
"""

my_theme={
    "palette":
    {
        "background": {"default": "green"}
    }
}

Gui(page).run(debug=True, use_reloader=True, theme=my_theme)




