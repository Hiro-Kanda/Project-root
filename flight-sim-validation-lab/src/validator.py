from src.models import State, ObservedState

def compute_final_metrics(states: list[State], observations: list[ObservedState]) -> dict:
  final_state = states[-1]
  final_observation = observations[-1]

  position_error = ((final_state.x - final_observation.x) ** 2 + (final_state.y - final_observation.y) ** 2) ** 0.5

  return {
    "flight_time": final_state.t,
    "final_x": final_state.x,
    "final_y": final_state.y,
    "position_error": round(position_error, 3),
  }