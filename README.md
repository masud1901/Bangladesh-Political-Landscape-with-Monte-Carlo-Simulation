# Bangladesh Election Simulation and Reverse Political Spectrum Inference Using Monte Carlo Simulation

This project consists of two key components:

1. A **Simulation Model** that simulates the political affiliations of individuals in Bangladesh based on demographic data and then simulates election outcomes based on these affiliations.
2. A **Reverse Simulation Model** that infers the underlying political spectrum distribution in the electorate from actual election results using optimization techniques.

## Project Structure

- `bangladesh_election_simulation.py`: This file contains the simulation model that simulates political affiliations and election outcomes based on demographic probabilities and historical election data.
- `reverse_simulation.py`: This file contains the reverse simulation model that infers the distribution of political spectrums based on actual election results.

---

## 1. Election Simulation Model

### Objective:
The goal of this model is to simulate individual political affiliations based on various demographic factors and assess whether the simulation reflects actual election outcomes.

### Steps:

- **Data and Constants**:
  - `load_data_and_constants`: Loads historical election data and initializes constants such as population size, religion, age, gender, education, and urban/rural distribution. This data is used to assign probabilities to various demographic factors.
  
- **Political Spectrum and Party Definition**:
  - `define_parties_and_spectrums`: Defines major political parties and their associated political spectrums (e.g., Awami League - Social Democracy, BNP - Conservatism, etc.).

- **Demographic Probability Mapping**:
  - `define_demographic_probabilities`: Assigns probabilities to how different demographic groups (based on religion, education, etc.) are likely to support various political parties.

- **Simulating Individuals**:
  - `simulate_individual`: Simulates the political affiliation of an individual by considering their demographic data (religion, age, education, etc.), the political spectrums of different parties, and historical voting probabilities.

- **Run Simulation**:
  - `run_simulation`: Simulates an entire population based on a specified number of individuals and generates the political affiliations of the population for a given election year.

- **Analyze Results**:
  - `analyze_results`: Compares the simulated political affiliation distribution to the actual election results, using historical election data for a specific year.

- **Statistical Analysis**:
  - `safe_chisquare`: Performs a chi-square test to determine how closely the simulated election results match the actual results.

### Usage:

Run the `simulation.py` script to simulate election outcomes based on demographic factors and historical data for a specified year. Example:

```bash
python simulation.py
```

## 2. Reverse Political Spectrum Inference Model

### Objective:
The reverse simulation model infers the distribution of political spectrums in the electorate using actual election results. By applying optimization techniques, the model finds the best-fitting political spectrum distribution that explains the election results.

### Steps:

- **Loading Election Results**:
  - `load_election_results`: Loads the actual vote shares for different parties from a CSV file for a given election year.

- **Expected Vote Calculation**:
  - `calculate_expected_votes`: Computes the expected vote shares for each party based on the distribution of political spectrums.

- **Objective Function for Optimization**:
  - `objective`: Defines the objective function to minimize the difference between actual vote shares and expected vote shares, based on the inferred political spectrum distribution.

- **Optimization**:
  - `infer_spectrum_distribution`: Uses the `scipy.optimize.minimize` function with constraints to find the optimal distribution of political spectrums that minimizes the difference between expected and actual election results.

### Usage:

Run the `reverse_simulation.py` script to infer the political spectrum distribution for a given election year. Example:

```bash
python reverse_simulation.py
```

---

## Data Requirements

- Historical election data: A CSV file (`bangladesh_elections_data.csv`) containing election results with columns: "Year", "Party", and "Vote Share (%)".

Example data format:

| Year | Party                         | Vote Share (%) |
|------|-------------------------------|----------------|
| 2001 | Awami League                  | 45.5           |
| 2001 | Bangladesh Nationalist Party  | 53.0           |
| 2001 | Jatiya Party                  | 1.5            |

## How It Works

### Simulation Flow

1. Load demographic data and assign political probabilities to demographic groups.
2. Simulate the political spectrum for each individual in the population based on their demographic attributes.
3. Adjust party probabilities based on individual political spectrums and demographic factors.
4. Aggregate the population's political affiliations and compare them to actual election results.
5. Perform statistical tests to evaluate the simulation's accuracy.

### Reverse Simulation Flow

1. Load actual election results for a given year.
2. Set up an optimization problem to minimize the difference between actual and expected vote shares.
3. Infer the most likely political spectrum distribution that explains the election results.

## Conclusion

This project provides insights into how demographics and political spectrums influence elections in Bangladesh. The simulation model allows us to experiment with various assumptions about demographics, while the reverse model helps infer the electorate's political spectrum based on real election data.

---

## Dependencies

- Python 3.x
- pandas
- numpy
- scipy

Install the required packages using:

```bash
pip install pandas numpy scipy
```

---

## License

This project is open-source and available under the MIT License.
