import pandas as pd
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

carbon_emission = np.random.randint(200, 600, 6)
energy_usage = np.random.randint(1000, 5000, 6)
water_consumption = np.random.randint(500, 3000, 6)

esg_df = pd.DataFrame({
    'Month': months,
    'Carbon_Emission': carbon_emission,
    'Energy_Usage': energy_usage,
    'Water_Consumption': water_consumption
})

esg_df.to_csv('esg_metrics.csv', index=False)

print('ESG dataset generated!')
