import numpy as np

def calculate_average_price(prices):
    return np.mean(prices)

def calculate_price_change(prices):
    return (prices[-1] - prices[0]) / prices[0] * 100
