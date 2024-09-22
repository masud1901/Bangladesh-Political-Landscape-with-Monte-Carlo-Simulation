from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import chisquare
import numpy as np

# Example simulated and real results
simulated_results = affiliation_counts.to_dict()  # From the Monte Carlo simulation
real_results = real_party_support["Votes (%)"].to_dict()  # From the election data

# Convert both into lists of values for easy comparison
simulated_values = [
    simulated_results[party]
    for party in real_results.keys()
    if party in simulated_results
]
real_values = [
    real_results[party] for party in real_results.keys() if party in simulated_results
]

# Mean Absolute Error (MAE)
mae = mean_absolute_error(real_values, simulated_values)
print(f"Mean Absolute Error (MAE): {mae}")

# Mean Squared Error (MSE)
mse = mean_squared_error(real_values, simulated_values)
print(f"Mean Squared Error (MSE): {mse}")

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# R-squared
r_squared = r2_score(real_values, simulated_values)
print(f"R-squared: {r_squared}")

# Chi-Square Test
chi_square, p_value = chisquare(f_obs=real_values, f_exp=simulated_values)
print(f"Chi-Square: {chi_square}, p-value: {p_value}")
