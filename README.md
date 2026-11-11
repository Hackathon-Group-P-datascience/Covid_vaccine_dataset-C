# Siraj Group P — Data Science Challenge Hackathon (Dataset C: COVID-19 Vaccine Allocation)

## Team Roster & Assigned Roles (Group P)
| # | Student Name | Student ID | Assigned Role & Individual Notebook | Presentation Section (17 Nov) |
|---|---|---|---|---|
| **1** | **Siraj Uddin Mohammad** | `24089738` | **R1 — Integrator & Git Lead:** `01_Siraj_Uddin_Mohammad_24089738_setup_and_integrity.ipynb`, `town_cost.py` | Team Workflow & Architecture |
| **2** | **Subhash Chandrupatla** | `24082089` | **R2 — EDA Lead A:** `02_Subhash_Chandrupatla_24082089_eda_target_and_missingness.ipynb` | EDA: Target & Missing Data |
| **3** | **Chapalabanda Praneeth Kumar** | `24080396` | **R3 — EDA Lead B:** `03_Chapalabanda_Praneeth_Kumar_24080396_eda_clinical_and_correlations.ipynb` | EDA: Clinical & Behavioural Drivers |
| **4** | **Karthik Sai Adithya Vasanth Yalakag** | `24079547` | **R4 — Metric Researcher:** `04_Karthik_Sai_Adithya_24079547_town_cost_metric_and_cutoffs.ipynb` | Task Metric & Decision Rule |
| **5** | **Jaya Krishna Katta** | `24100682` | **R5 — Pre-processing Lead:** `05_Jaya_Krishna_Katta_24100682_preprocessing_and_ablation.ipynb` | Pre-processing & Feature Engineering |
| **6** | **Pravinya Rayalapati** | `24099441` | **R6 — Modeller A (Baselines & Calibration):** `06_Pravinya_Rayalapati_24099441_baseline_models_and_calibration.ipynb` | Baseline Models & Calibration |
| **7** | **Muhammad Dawood Aslam** | `24065392` | **R7 — Modeller B (Gradient Boosting & Tuning):** `07_Muhammad_Dawood_Aslam_24065392_hyperparameter_tuning.ipynb` | Gradient Boosting & Tuning |
| **8** | **Bhanu Prakash Mallam** | `24095576` | **R8 — Modeller C (Ensembling & Robustness):** `08_Bhanu_Prakash_Mallam_24095576_ensembles_and_sensitivity.ipynb` | Ensembles & Sensitivity Analysis |
| **9** | **Syed Nadeem Ali** | `24065385` | **R9 — XAI, Submissions & Stakeholder Lead:** `09_Syed_Nadeem_Ali_24065385_xai_and_final_submissions.ipynb` | Explainable AI & Stakeholder Summary |

## Repository Deliverables
* **Master Notebook:** `00_FINAL_GroupP_TownCost.ipynb`
* **Metric Module:** `town_cost.py`
* **5 Ranked Test Predictions (Best to Worst by 15-Fold CV Town Cost per Resident):**
  1. `challenge_submission_group_P_order_1.csv` (`SoftVoting_Blend` — $3,298.21/resident)
  2. `challenge_submission_group_P_order_2.csv` (`LightGBM` — $3,299.48/resident)
  3. `challenge_submission_group_P_order_3.csv` (`LightGBM_Tuned` — $3,300.51/resident)
  4. `challenge_submission_group_P_order_4.csv` (`Stacked_Generaliser` — $3,300.83/resident)
  5. `challenge_submission_group_P_order_5.csv` (`HGB_Tuned` — $3,302.07/resident)
* **Summary Manifest:** `ranking.csv`
