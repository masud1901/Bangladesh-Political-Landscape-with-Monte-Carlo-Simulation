import numpy as np
import pandas as pd
import random
from scipy import stats


# Load data and constants
def load_data_and_constants():
    historical_data = pd.read_csv("bangladesh_elections_data.csv")

    constants = {
        "population_size": 1000,
        "religion_distribution": {
            "Islam": 0.9104,
            "Hinduism": 0.0795,
            "Buddhism": 0.0061,
            "Christianity": 0.0030,
            "Others": 0.0012,
        },
        "age_distribution": {"18-30": 0.35, "31-50": 0.40, "51-65": 0.15, "65+": 0.10},
        "gender_distribution": {"Male": 0.50, "Female": 0.49, "Other": 0.01},
        "literacy_rate": {"Literate": 0.7467, "Illiterate": 0.2533},
        "urban_rural_distribution": {"Urban": 0.3743, "Rural": 0.6257},
    }

    education_data = {
        "None": 19376,
        "Primary": 15699,
        "Secondary": 18710,
        "Higher Secondary": 3637,
        "Tertiary": 3209,
        "Others": 197,
    }
    total_education = sum(education_data.values())
    constants["education_distribution"] = {
        k: v / total_education for k, v in education_data.items()
    }

    return historical_data, constants


# Define parties and political spectrums
def define_parties_and_spectrums():
    parties = {
        "Awami League": "Social Democracy",
        "Bangladesh Nationalist Party": "Conservatism",
        "Bangladesh Jamaat-e-Islami": "Islamic Theocracy",
        "Jatiya Party": "Populism",
        "Independents": "Various",
    }

    political_spectrums = {
        "Communism": {"18-30": 0.05, "31-50": 0.03, "51-65": 0.02, "65+": 0.01},
        "Social Democracy": {"18-30": 0.30, "31-50": 0.25, "51-65": 0.20, "65+": 0.15},
        "Progressivism": {"18-30": 0.25, "31-50": 0.20, "51-65": 0.15, "65+": 0.10},
        "Conservatism": {"18-30": 0.15, "31-50": 0.25, "51-65": 0.30, "65+": 0.35},
        "Republican Patriotism": {
            "18-30": 0.10,
            "31-50": 0.15,
            "51-65": 0.20,
            "65+": 0.25,
        },
        "Tribalism": {"18-30": 0.05, "31-50": 0.07, "51-65": 0.08, "65+": 0.09},
        "Islamic Theocracy": {"18-30": 0.05, "31-50": 0.03, "51-65": 0.03, "65+": 0.03},
        "Populism": {"18-30": 0.05, "31-50": 0.02, "51-65": 0.02, "65+": 0.02},
    }

    return parties, political_spectrums


# Define demographic probabilities
def define_demographic_probabilities():
    return {
        "religion": {
            "Awami League": {
                "Islam": 0.55,
                "Hinduism": 0.65,
                "Buddhism": 0.55,
                "Christianity": 0.55,
                "Others": 0.50,
            },
            "Bangladesh Nationalist Party": {
                "Islam": 0.40,
                "Hinduism": 0.30,
                "Buddhism": 0.35,
                "Christianity": 0.35,
                "Others": 0.40,
            },
            "Bangladesh Jamaat-e-Islami": {
                "Islam": 0.15,
                "Hinduism": 0.02,
                "Buddhism": 0.05,
                "Christianity": 0.05,
                "Others": 0.05,
            },
            "Jatiya Party": {
                "Islam": 0.05,
                "Hinduism": 0.05,
                "Buddhism": 0.10,
                "Christianity": 0.10,
                "Others": 0.10,
            },
            "Independents": {
                "Islam": 0.05,
                "Hinduism": 0.08,
                "Buddhism": 0.10,
                "Christianity": 0.10,
                "Others": 0.15,
            },
        },
        "education": {
            "Awami League": {
                "None": 0.50,
                "Primary": 0.55,
                "Secondary": 0.58,
                "Higher Secondary": 0.60,
                "Tertiary": 0.62,
                "Others": 0.55,
            },
            "Bangladesh Nationalist Party": {
                "None": 0.40,
                "Primary": 0.35,
                "Secondary": 0.32,
                "Higher Secondary": 0.30,
                "Tertiary": 0.28,
                "Others": 0.35,
            },
            "Bangladesh Jamaat-e-Islami": {
                "None": 0.15,
                "Primary": 0.12,
                "Secondary": 0.10,
                "Higher Secondary": 0.08,
                "Tertiary": 0.06,
                "Others": 0.10,
            },
            "Jatiya Party": {
                "None": 0.10,
                "Primary": 0.10,
                "Secondary": 0.10,
                "Higher Secondary": 0.10,
                "Tertiary": 0.10,
                "Others": 0.10,
            },
            "Independents": {
                "None": 0.05,
                "Primary": 0.08,
                "Secondary": 0.10,
                "Higher Secondary": 0.12,
                "Tertiary": 0.14,
                "Others": 0.10,
            },
        },
    }


# Get party probabilities based on historical data
def get_party_probabilities(historical_data, year, parties):
    year_data = historical_data[historical_data["Year"] == year]
    probabilities = year_data.set_index("Party")["Vote Share (%)"] / 100
    return {party: probabilities.get(party, 0.01) for party in parties.keys()}


# Simulate an individual
def simulate_individual(
    year,
    constants,
    parties,
    political_spectrums,
    demographic_probabilities,
    historical_data,
):
    individual = {
        "religion": random.choices(
            list(constants["religion_distribution"].keys()),
            weights=constants["religion_distribution"].values(),
        )[0],
        "age_group": random.choices(
            list(constants["age_distribution"].keys()),
            weights=constants["age_distribution"].values(),
        )[0],
        "gender": random.choices(
            list(constants["gender_distribution"].keys()),
            weights=constants["gender_distribution"].values(),
        )[0],
        "literacy": random.choices(
            list(constants["literacy_rate"].keys()),
            weights=constants["literacy_rate"].values(),
        )[0],
        "location": random.choices(
            list(constants["urban_rural_distribution"].keys()),
            weights=constants["urban_rural_distribution"].values(),
        )[0],
        "education": random.choices(
            list(constants["education_distribution"].keys()),
            weights=constants["education_distribution"].values(),
        )[0],
    }

    spectrum_probs = [
        political_spectrums[spectrum][individual["age_group"]]
        for spectrum in political_spectrums
    ]
    individual["political_spectrum"] = random.choices(
        list(political_spectrums.keys()), weights=spectrum_probs
    )[0]

    base_probabilities = get_party_probabilities(historical_data, year, parties)
    adjusted_probabilities = base_probabilities.copy()

    for party in parties.keys():
        for factor in ["religion", "education"]:
            if party in demographic_probabilities[factor]:
                adjusted_probabilities[party] *= demographic_probabilities[factor][
                    party
                ].get(individual[factor], 1.0)

        if parties[party] == individual["political_spectrum"]:
            adjusted_probabilities[party] *= 1.5
        elif parties[party] in ["Various", "Populism"]:
            adjusted_probabilities[party] *= 1.2

    total = sum(adjusted_probabilities.values())
    adjusted_probabilities = {
        party: prob / total for party, prob in adjusted_probabilities.items()
    }

    individual["political_affiliation"] = random.choices(
        list(adjusted_probabilities.keys()), weights=adjusted_probabilities.values()
    )[0]

    return individual


# Run simulation
def run_simulation(
    num_simulations,
    year,
    constants,
    parties,
    political_spectrums,
    demographic_probabilities,
    historical_data,
):
    individuals = [
        simulate_individual(
            year,
            constants,
            parties,
            political_spectrums,
            demographic_probabilities,
            historical_data,
        )
        for _ in range(num_simulations)
    ]
    return pd.DataFrame(individuals)


# Analyze results
def analyze_results(simulated_population, historical_data, year):
    simulated_results = (
        simulated_population["political_affiliation"].value_counts(normalize=True) * 100
    )
    real_results = historical_data[historical_data["Year"] == year][
        ["Party", "Vote Share (%)"]
    ].set_index("Party")

    all_parties = set(simulated_results.index) | set(real_results.index)
    aligned_results = {party: {"simulated": 0, "real": 0} for party in all_parties}

    for party in all_parties:
        if party in simulated_results.index:
            aligned_results[party]["simulated"] = simulated_results[party]
        if party in real_results.index:
            aligned_results[party]["real"] = real_results.loc[party, "Vote Share (%)"]

    observed = np.array([aligned_results[party]["simulated"] for party in all_parties])
    expected = np.array([aligned_results[party]["real"] for party in all_parties])
    observed = observed * (sum(expected) / sum(observed))

    return simulated_results, real_results, aligned_results, observed, expected


# Perform chi-square test
def safe_chisquare(observed, expected, epsilon=1e-8):
    observed, expected = np.array(observed), np.array(expected)
    expected = expected + epsilon
    observed = observed * (sum(expected) / sum(observed))
    chi2 = np.sum((observed - expected) ** 2 / expected)
    df = len(observed) - 1
    p_value = 1 - stats.chi2.cdf(chi2, df)
    return chi2, p_value


# Main function
def main():
    historical_data, constants = load_data_and_constants()
    parties, political_spectrums = define_parties_and_spectrums()
    demographic_probabilities = define_demographic_probabilities()

    year = 2001
    simulated_population = run_simulation(
        constants["population_size"],
        year,
        constants,
        parties,
        political_spectrums,
        demographic_probabilities,
        historical_data,
    )

    simulated_results, real_results, aligned_results, observed, expected = (
        analyze_results(simulated_population, historical_data, year)
    )

    print("Simulated Political Affiliation Distribution for 2008 (%):")
    print(simulated_results)
    print("\nReal Election Results for 2008 (%):")
    print(real_results)

    print("\nAligned Results:")
    for party in aligned_results:
        sim = aligned_results[party]["simulated"]
        real = aligned_results[party]["real"]
        diff = sim - real
        print(
            f"{party}: Simulated {sim:.2f}%, Real {real:.2f}%, Difference {diff:.2f}%"
        )

    chi2, p_value = safe_chisquare(observed, expected)
    print("\nHypothesis Test Results:")
    print(f"Chi-square statistic: {chi2}")
    print(f"p-value: {p_value}")

    if p_value < 0.05:
        print(
            "The simulation results are significantly different from the real results."
        )
    else:
        print(
            "The simulation results are not significantly different from the real results."
        )


if __name__ == "__main__":
    main()
