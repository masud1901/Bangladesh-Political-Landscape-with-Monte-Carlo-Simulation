import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_spectrum_distribution(inferred_distribution, year):
    """
    Create a horizontal bar chart of the inferred political spectrum distribution.
    """
    plt.figure(figsize=(12, 8))
    spectrums = list(inferred_distribution.keys())
    values = list(inferred_distribution.values())

    # Sort by values
    spectrums, values = zip(
        *sorted(zip(spectrums, values), key=lambda x: x[1], reverse=True)
    )

    plt.barh(spectrums, values)
    plt.xlabel("Probability")
    plt.ylabel("Political Spectrum")
    plt.title(f"Inferred Political Spectrum Distribution for {year}")

    # Add value labels on the bars
    for i, v in enumerate(values):
        plt.text(v, i, f"{v:.2%}", va="center")

    plt.tight_layout()
    plt.savefig(f"spectrum_distribution_{year}.png")
    plt.close()


def plot_vote_comparison(actual_votes, expected_votes, year):
    """
    Create a grouped bar chart comparing actual and expected vote shares.
    """
    plt.figure(figsize=(12, 8))
    parties = list(actual_votes.index)
    x = np.arange(len(parties))
    width = 0.35

    plt.bar(x - width / 2, actual_votes, width, label="Actual")
    plt.bar(
        x + width / 2,
        [expected_votes.get(party, 0) for party in parties],
        width,
        label="Expected",
    )

    plt.xlabel("Parties")
    plt.ylabel("Vote Share")
    plt.title(f"Actual vs Expected Vote Shares for {year}")
    plt.xticks(x, parties, rotation=45, ha="right")
    plt.legend()

    plt.tight_layout()
    plt.savefig(f"vote_comparison_{year}.png")
    plt.close()


def plot_spectrum_trends(spectrum_data):
    """
    Create a line plot showing trends in political spectrum distributions over time.

    spectrum_data should be a dictionary where keys are years and values are
    the inferred_distribution dictionaries for those years.
    """
    plt.figure(figsize=(12, 8))

    for spectrum in political_spectrums:
        values = [data[spectrum] for data in spectrum_data.values()]
        plt.plot(spectrum_data.keys(), values, marker="o", label=spectrum)

    plt.xlabel("Year")
    plt.ylabel("Probability")
    plt.title("Political Spectrum Distribution Trends")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.savefig("spectrum_trends.png")
    plt.close()


def plot_heatmap(spectrum_data):
    """
    Create a heatmap showing the evolution of political spectrum distributions over time.

    spectrum_data should be a dictionary where keys are years and values are
    the inferred_distribution dictionaries for those years.
    """
    df = pd.DataFrame(spectrum_data).T

    plt.figure(figsize=(12, 8))
    sns.heatmap(df, annot=True, fmt=".2%", cmap="YlOrRd")

    plt.xlabel("Political Spectrum")
    plt.ylabel("Year")
    plt.title("Evolution of Political Spectrum Distributions")

    plt.tight_layout()
    plt.savefig("spectrum_heatmap.png")
    plt.close()


# Add these function calls in your main function
def main():
    # ... (your existing code)

    # Single year visualizations
    plot_spectrum_distribution(inferred_distribution, year)
    plot_vote_comparison(actual_votes, expected_votes, year)

    # Multi-year visualizations (you'll need to run your analysis for multiple years first)
    spectrum_data = {
        2008: inferred_distribution,
        # Add more years here
        # 2012: inferred_distribution_2012,
        # 2016: inferred_distribution_2016,
        # etc.
    }

    plot_spectrum_trends(spectrum_data)
    plot_heatmap(spectrum_data)


if __name__ == "__main__":
    main()
