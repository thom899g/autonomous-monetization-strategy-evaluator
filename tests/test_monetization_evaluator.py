import pytest
from monetization_strategy_evaluator import MonetizationStrategyEvaluator

@pytest.fixture
def evaluator():
    return MonetizationStrategyEvaluator()

def test_evaluate_strategy_success(evaluator):
    strategy = {"name": "Basic Pricing", "feasibility": 90}
    result = evaluator.evaluate_strategy(strategy)
    assert result["status"] == "success"
    assert "evaluation_score" in result

def test_assess_risks_high_risk(evaluator):
    risks