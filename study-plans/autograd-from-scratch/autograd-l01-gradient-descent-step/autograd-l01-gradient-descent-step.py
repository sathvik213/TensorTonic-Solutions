
import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:

    values = np.array(values, dtype=np.float64)
    gradients = np.array(gradients, dtype=np.float64)

    updated_values = values - learning_rate * gradients

    predicted_change = np.dot(
        gradients, np.array(updated_values) - values
    )

    return updated_values.tolist(), float(predicted_change)
