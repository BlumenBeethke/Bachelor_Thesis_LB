import numpy as np
from scipy.stats import norm
import pandas as pd

# List of valid option types
option_types = ["call", "put"]

def black_scholes_merton(S, K, T, r, sigma, option_type) -> float:
    
    """
    Calculate the theoretical option price by using the Black-Scholes-Merton formula.

    Args:
        S (float): Current underlying price
        K (float): Strike price, also so-called exercise price
        T (float): Time to expiration (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the underlying
        option_type (str): 'call' or 'put'

    Returns:
        float: Calculated theoretical Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * (T)) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    assert option_type in option_types, f"{option_type} is not in the defined option types list"
    
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * (T)) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * (T)) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return option_price

def parkinson_volatility(high, low, trading_days: int = 252) -> float:
    """
    Einfache historische Volatilität (Parkinson) aus High/Low.
    Akzeptiert Skalar, Liste oder NumPy-Array. Gibt einen float (annualisiert) zurück.
    """
    h = np.atleast_1d(np.asarray(high, dtype=float))
    l = np.atleast_1d(np.asarray(low,  dtype=float))
    lr = np.log(h / l)                              # log-Range
    daily_var = (lr * lr) / (4.0 * np.log(2.0))     # Tagesvarianz
    return float(np.sqrt(daily_var.mean() * trading_days))


def interest_rate_forward(S, T, F) -> float:
    """
    Calculate the interest rate fbased on forward price.

    Args:
        S (float): Current underlying price
        T (float): Time to expiration (in years)
        F (float): Forward price

    Returns:
        float: Calculated interest rate, r 
    """
   
    assert S > 0, f"Underlying price {S} must be greater than zero"
    assert F > 0, f"Forward price {F} must be greater than zero"  
    
    try:
        r = (np.log(F) - np.log(S)) / T

        if np.isnan(r):
            return 0
        
        return r
    
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        
        return 0
    

# Beispielaufruf / Example usage of Black Sholes Merton formula
# S = 4943.5      # Aktueller Aktienkurs
# K = 4900        # Ausübungspreis / Excercise price
#T = 0.161644    # Zeit bis zur Fälligkeit in Jahren / Time to expiration (in years)
#r = 0.05        # Risikofreier Zinssatz /Risk-free interest rate
#sigma = 0.2     # Volatility / Volatilität
#sigma = 0.13682 # Volatilität / Volatilität
#F = 4943.5      # Forward-Preis

#interest_rate = interest_rate_forward(S, T, F)
#print(f"Forward-Zinssatz: {interest_rate:.2f}")

#option_type = 'call'
#call_price = black_scholes_merton(S, K, T, r, sigma, option_type)
#print(f"Call-Option Preis: {call_price:.2f}")

#option_type = 'put'
#put_price = black_scholes_merton(S, K, T, r, sigma, option_type)
#print(f"Put-Option Preis: {put_price:.2f}")


# Example usage of Black Sholes Merton formula
#S0 = 100     # Current underlying price
#K = 105      # Strike / Exercise price
#T = 1.0      # Time to expiration (in years)
#r = 0.05     # Risk-free interest rate
#sigma = 0.2  # Volatility
#option_type = 'call'  # 'call' option

# a Call option
#option_price = black_scholes_merton(S0, K, T, r, sigma, option_type)
#print("Theoretical Option price with option type {} = {}".format(option_type, option_price))

# a Put option
#option_type = 'put'  # 'put' option
#option_price = black_scholes_merton(S0, K, T, r, sigma, option_type)
#print("Theoretical Option price with option type {} = {}".format(option_type, option_price))
