import torch
from taipy import Gui, NumberInput

# Define the linear regression model
class LinearRegression(torch.nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(3, 1)  # One input, one output

    def forward(self, x):
        return self.linear(x)

# Create some sample data
x_data = torch.tensor([1.0, 2.0, 3.0])
y_data = torch.tensor([2.0, 4.0, 6.0])

# Train the model (replace with your actual training loop)
model = LinearRegression()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(100):
    # Forward pass
    y_pred = model(x_data)
    loss = torch.nn.functional.mse_loss(y_pred, y_data)

    # Backward pass and update weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Create the Taipy GUI
app = Gui()

# Input field for user to enter a value
x_input = app.NumberInput(label="Enter a value (x):")

# Function to make predictions using the model
def predict(evt):
    x = torch.tensor([evt.value])
    y_pred = model(x)
    app.update_label(result_label, f"Predicted y: {y_pred.item():.2f}")

# Button to trigger prediction
predict_button = app.Button(text="Predict", command=predict)

# Label to display the prediction result
result_label = app.Label(text="Result:")

# Layout the UI elements
app.row(x_input, predict_button)
app.column(result_label)

# Run the Taipy application
app.run()
