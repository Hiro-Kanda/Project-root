from src.models import State
from src.simulator import run_simulation
from src.validator import compute_final_metrics


def test_simulation_runs() -> None:
  initial = State(t=0.0, x=0.0, y=10.0, vx=5.0, vy=8.0)
  states, observations = run_simulation(initial_state=initial, dt=0.1, steps=50)

  assert len(states) >= 2
  assert len(states) == len(observations)


def test_metrics_exist() -> None:
  initial = State(t=0.0, x=0.0, y=10.0, vx=5.0, vy=8.0)
  states, observations = run_simulation(initial_state=initial, dt=0.1, steps=50)
  metrics = compute_final_metrics(states, observations)

  assert "flight_time" in metrics
  assert "final_x" in metrics
  assert "position_error" in metrics