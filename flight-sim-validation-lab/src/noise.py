import random

from src.models import ObservedState, State

def observe_state(state: State, noise_scale: float = 0.05) -> ObservedState:
  return ObservedState(
    t=state.t,
    x=round(state.x + random.uniform(-noise_scale, noise_scale), 3),
    y=round(state.y + random.uniform(-noise_scale, noise_scale), 3),
  )