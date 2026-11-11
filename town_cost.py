"""Town-cost metric and helper utilities for Dataset C (Nov 2026 Hackathon — Siraj Group P).

Economic rules from 'Dataset C Information.pdf' and 'Target Metric Information':
  * 100% infection probability across the town due to winter indoor gatherings.
  * Vaccine cost V = $1,500 per dose posted to a resident's home (wasted if refused).
  * Legal mandate: anyone who WANTS a vaccine (y=1) but is not sent one (s=0) must be
    compensated V = $1,500 in cash, and remains unvaccinated.
  * Hospitalisation cost H = $41,000 per stay.
  * Unvaccinated hospitalisation probability p_u depends on age_group and number_chronic_med_conditions.
  * Vaccinated hospitalisation probability p_v = p_u * (1 - VE).

Bayes-optimal personal threshold for resident i with acceptance probability q_i:
  Send vaccine (s_i = 1) iff q_i > V / (V + (p_{u,i} - p_{v,i}) * H).
"""
import numpy as np
import pandas as pd

VACCINE_COST = 1_500.0        # $ per dose (Dataset C Information page 2)
HOSP_COST = 41_000.0          # $ per COVID-19 hospitalisation (Dataset C Information page 2)
VACC_EFFECTIVENESS = 0.80     # Relative reduction in hospitalisation risk when vaccinated

P_HOSP_AGE = {
    "18 - 34 Years": 0.015,
    "35 - 44 Years": 0.025,
    "45 - 54 Years": 0.040,
    "55 - 64 Years": 0.070,
    "65+ Years": 0.150,
}
CHRONIC_MULTIPLIER = 1.50
CHRONIC_COL = "number_chronic_med_conditions"


def compute_hosp_risks(
    df: pd.DataFrame,
    p_age: dict = None,
    ve: float = VACC_EFFECTIVENESS,
    chronic_mult: float = CHRONIC_MULTIPLIER,
):
    """Return (p_unvaccinated, p_vaccinated) arrays for each row of df."""
    p_age = p_age or P_HOSP_AGE
    base_p = df["age_group"].map(p_age).fillna(np.mean(list(p_age.values()))).to_numpy(dtype=float)
    n_chronic = df[CHRONIC_COL].fillna(0).clip(lower=0).to_numpy(dtype=float)
    p_u = np.clip(base_p * (chronic_mult ** n_chronic), 0.0, 1.0)
    return p_u, p_u * (1.0 - ve)


def town_total_cost(y_true, sent_decision, p_u, p_v, V: float = VACCINE_COST, H: float = HOSP_COST) -> float:
    """Total expenditure ($) by the town. Lower is better."""
    y_b = np.asarray(y_true, dtype=int)
    s_b = np.asarray(sent_decision, dtype=int)
    vaccine_spend = V * ((s_b == 1) | (y_b == 1))
    hosp_spend = H * np.where((s_b == 1) & (y_b == 1), p_v, p_u)
    return float(np.sum(vaccine_spend + hosp_spend))


def personal_cutoff(p_u, p_v, V: float = VACCINE_COST, H: float = HOSP_COST):
    """Person-specific probability cut-off tau_i."""
    return V / (V + (p_u - p_v) * H)


def optimal_send_decision(q_prob, p_u, p_v, V: float = VACCINE_COST, H: float = HOSP_COST):
    """Binary decision (1 = post vaccine, 0 = do not post) minimising expected town expenditure."""
    return (np.asarray(q_prob, dtype=float) > personal_cutoff(p_u, p_v, V, H)).astype(int)
