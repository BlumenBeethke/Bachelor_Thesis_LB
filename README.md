# Bachelor-Thesis_LB

Code and thesis for my Bachelor's thesis in Mathematics at Heidelberg University:
**"Künstliche neuronale Netze für die Preisbestimmung von europäischen Optionen"**
(Artificial Neural Networks for Pricing European Options).

The thesis was written in 2024 at Deutsche Börse AG and supervised by Prof. Dr. Enno Mammen (submitted 14.01.2025, grade 1.0). It trains neural networks on real production data of EURO STOXX 50 index options (OESX) to approximate Black-Scholes-Merton prices. A logarithmic transformation of the input data improves the results compared to the untransformed data. The thesis itself is written in German.

## Models

Two networks are trained on the same features and compared with the Black-Scholes-Merton price:

- **scikit-learn `MLPRegressor`**: three hidden layers with 128 neurons, ReLU, Adam, batch size 128, 80/20 train/test split.
- **Keras `Sequential`**: dense layers with 128, 128, 128 and 64 neurons (ReLU), Adam with learning rate 0.001, MSE loss, 256 epochs, batch size 64, 20 % validation split. Layer sizes are set in `Configuration.yml`.

Both are evaluated with MSE and MAE on the held-out test set. The notebook also compares training time.

## Data

The OESX production data was provided by Deutsche Börse AG and is **not part of this repository**. The notebook expects a semicolon-separated file `trainings_data_with_vola_time.csv` in the working directory. According to the thesis, the data covers four trading days in 2024 and contains the columns listed under `features` in `Configuration.yml` (underlying, exercise price, forward price, interest rate, volatility, time to expiration, theoretical price).

Without this file the notebook cannot be run from start to finish, but `BlackScholes.py` works on its own.

## Setup

```bash
pip install numpy pandas scipy scikit-learn keras tensorflow plotly matplotlib pyyaml QuantLib
```

The first cells of the notebook also install `seaborn`, `pydot`, `graphviz`, `nbformat` and `keras-layer-normalization`.

## Usage

Black-Scholes-Merton price of a European option:

```python
from BlackScholes import black_scholes_merton

price = black_scholes_merton(S=100, K=105, T=1.0, r=0.05, sigma=0.2, option_type="call")
```

To rerun the experiments, place the CSV file next to the notebook, adjust the filter in `Configuration.yml` if needed, and run `Playground_15.10-2.ipynb` from top to bottom.

## Author

Lennart Bethke
