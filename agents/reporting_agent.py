import requests
import json
import random

class ReportingAgent:
    def __init__(self, qlik_app_id: str = "dummy_app"):
        self.qlik_app_id = qlik_app_id

    def validate_chart_total(self, chart_name: str, backend_total: float) -> dict:
        # Simulate Qlik API response (in real use, call Qlik Engine API)
        simulated_qlik_total = backend_total * (1 + random.uniform(-0.005, 0.005))
        variance_pct = abs(simulated_qlik_total - backend_total) / backend_total * 100 if backend_total != 0 else 0
        
        return {
            "chart": chart_name,
            "qlik_total": round(simulated_qlik_total, 2),
            "backend_total": backend_total,
            "variance_pct": round(variance_pct, 3),
            "max_allowed_variance": 0.5,
            "passed": variance_pct <= 0.5,
            "status": "PASS" if variance_pct <= 0.5 else "FAIL"
        }

    def validate_all_charts(self, chart_configs: list) -> list:
        results = []
        for config in chart_configs:
            result = self.validate_chart_total(config["name"], config["expected_total"])
            results.append(result)
        return results

if __name__ == "__main__":
    agent = ReportingAgent()
    charts = [
        {"name": "Monthly Sales", "expected_total": 4250000.00},
        {"name": "Customer Count", "expected_total": 15872},
        {"name": "Avg Order Value", "expected_total": 267.50}
    ]
    results = agent.validate_all_charts(charts)
    for r in results:
        print(f"{r['chart']}: {r['status']} ({r['variance_pct']}%)")