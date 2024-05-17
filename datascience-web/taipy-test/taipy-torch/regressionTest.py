import torch

# Define the linear regression model
class LinearRegression(torch.nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(3, 1)  # One input, one output

    def forward(self, x):
        return self.linear(x)

# Create some sample data
x_data = torch.tensor([1.0, 2.0, 3.0])
y_data = torch.tensor([2.0])

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