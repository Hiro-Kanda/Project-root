from src.dynamics import step_state
from src.models import State
from src.noise import observe_state

def run_simulation(
  initial_state: State,
  dt: float,
  steps: int,
  wind_ax: float = 0.0,
  noise_scale: float = 0.05,
) -> tuple[list[State], list]:
  states = [initial_state]
  observations = [observe_state(initial_state, noise_scale=noise_scale)]

  current = initial_state
  for _ in range(steps):
    current = step_state(current, dt=dt, wind_ax=wind_ax)
    states.append(current)
    observations.append(observe_state(current, noise_scale=noise_scale))

    if current.y <= 0.0:
      break

    return states, observations