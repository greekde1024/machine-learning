import matplotlib.pyplot as plt

class LinearModel:
    def __init__(self):
        self.omega = 0
        self.b = 0

    def fit(self, x_train, y_train):
        self.omega = (y_train[0] - y_train[1]) / (x_train[0] - x_train[1])
        self.b = y_train[0] - x_train[0] * self.omega

    def predict(self, x):
        return self.omega * x + self.b


def main():
    X = [0, 0]
    Y = [0, 0]
    X[0], Y[0], X[1], Y[1] = map(float, input("Input x1 y1 x2 y2: ").split())
    
    lm = LinearModel()
    lm.fit(X, Y)
    print(f"Training result: omega={lm.omega}, b={lm.b}\n")
    
    x = float(input("Input x: "))
    y = lm.predict(x)
    print(f"Predict result: x={x:.2f}平米, y={y:.2f}万元")

    # Plotting the results
    plt.scatter(X, Y, color='blue', label='Training Data')
    
    # Plot the regression line
    x_vals = [min(X) - 1, x]  # Adding a little space beyond the training data
    y_vals = [lm.predict(x) for x in x_vals]
    
    plt.plot(x_vals, y_vals, color='red', label='Regression Line')

    # Mark the predicted point
    plt.scatter(x, y, color='green', label='Prediction')

    plt.xlabel('X (平米)')
    plt.ylabel('Y (万元)')
    plt.title('Linear Regression Result')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
