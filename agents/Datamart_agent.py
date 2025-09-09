import pandas as pd
from sklearn.ensemble import IsolationForest
import random

class DatamartAgent:
    def __init__(self):
        self.model = None
        self.historical_data = pd.DataFrame({
            'test_name': ['sales_sum', 'customer_count', 'avg_order_value'],
            'diff_pct': [0.1, -0.3, 0.8]
        })

    def train_tolerance_model(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.model.fit(self.historical_data[['diff_pct']])

    def is_within_tolerance(self, current_diff: float) -> bool:
        if self.model is None:
            self.train_tolerance_model()
        
        # Predict if point is anomaly (-1) or normal (1)
        pred = self.model.predict([[current_diff]])
        return pred[0] == 1

    def validate_metric(self, metric_name: str, actual: float, expected: float) -> dict:
        diff_pct = ((actual - expected) / expected) * 100 if expected != 0 else 0
        within_tolerance = self.is_within_tolerance(diff_pct)
        
        return {
            "metric": metric_name,
            "actual": actual,
            "expected": expected,
            "diff_pct": round(diff_pct, 2),
            "within_tolerance": within_tolerance,
            "status": "PASS" if within_tolerance else "FAIL"
        }

if __name__ == "__main__":
    agent = DatamartAgent()
    result = agent.validate_metric("monthly_sales", 1050000, 1045000)
    print(result)