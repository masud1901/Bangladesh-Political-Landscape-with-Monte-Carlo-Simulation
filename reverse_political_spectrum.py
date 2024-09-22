import numpy as np
import pandas as pd
import random
from scipy.optimize import minimize


# Load election results
def load_election_results(file_path, year):
    df = pd.read_csv(file_path)
    return df[df["Year"] == year].set_index("Party")["Vote Share (%)"] / 100


# Define parties and their associated political spectrums
parties_spectrum = {
    "Awami League": "Social Democracy",
    "Bangladesh Nationalist Party": "Conservatism",
    "Bangladesh Jamaat-e-Islami": "Islamic Theocracy",
    "Jatiya Party": "Populism",
    "Independents": "Various",
}

# Define political spectrums
political_spectrums = [
    "Communism",
    "Social Democracy",
    "Progressivism",
    "Conservatism",
    "Republican Patriotism",
    "Tribalism",
    "Islamic Theocracy",
    "Populism",
]


# Function to calculate expected vote share given spectrum distribution
def calculate_expected_votes(spectrum_distribution, parties_spectrum):
    expected_votes = {party: 0 for party in parties_spectrum}
    for party, spectrum in parties_spectrum.items():
        if spectrum in spectrum_distribution:
            expected_votes[party] = spectrum_distribution[spectrum]
        elif spectrum == "Various":
            expected_votes[party] = sum(spectrum_distribution.values()) / len(
                spectrum_distribution
            )
    return expected_votes


# Objective function to minimize (sum of squared differences)
def objective(x, actual_votes, parties_spectrum, political_spectrums):
    spectrum_distribution = dict(zip(political_spectrums, x))
    expected_votes = calculate_expected_votes(spectrum_distribution, parties_spectrum)
    return sum(
        (expected_votes[party] - actual_votes[party]) ** 2
        for party in actual_votes.index
    )


# Constraint: sum of probabilities should be 1
def constraint(x):
    return np.sum(x) - 1


# Infer political spectrum distribution
def infer_spectrum_distribution(actual_votes, parties_spectrum, political_spectrums):
    initial_guess = np.ones(len(political_spectrums)) / len(political_spectrums)
    bounds = [(0, 1) for _ in political_spectrums]
    constraint = {"type": "eq", "fun": lambda x: np.sum(x) - 1}

    result = minimize(
        objective,
        initial_guess,
        args=(actual_votes, parties_spectrum, political_spectrums),
        method="SLSQP",
        bounds=bounds,
        constraints=constraint,
    )

    return dict(zip(political_spectrums, result.x))


# Main function
def main():
    # Load actual election results
    year = 2008  # You can change this to analyze different years
    actual_votes = load_election_results("bangladesh_elections_data.csv", year)

    # Infer political spectrum distribution
    inferred_distribution = infer_spectrum_distribution(
        actual_votes, parties_spectrum, political_spectrums
    )

    # Print results
    print(f"Inferred Political Spectrum Distribution for {year}:")
    for spectrum, probability in sorted(
        inferred_distribution.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{spectrum}: {probability:.2%}")

    # Calculate and print expected votes based on inferred distribution
    expected_votes = calculate_expected_votes(inferred_distribution, parties_spectrum)
    print(f"\nComparison of Actual vs Expected Vote Shares for {year}:")
    for party in actual_votes.index:
        actual = actual_votes[party]
        expected = expected_votes.get(party, 0)
        diff = actual - expected
        print(
            f"{party}: Actual {actual:.2%}, Expected {expected:.2%}, Difference {diff:.2%}"
        )


if __name__ == "__main__":
    main()
