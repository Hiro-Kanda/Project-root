from src.models import State

def step_state(state: State, dt: float, wind_ax: float = 0.0) -> State:
  g = -9.8

  new_vx = state.vx + wind_ax * dt
  new_vy = state.vy + g * dt

  new_x = state.x + new_vx * dt
  new_y = max(0.0, state.y + new_vy * dt)

  return State(
    t=round(state.t + dt, 3),
    x=round(new_x, 3),
    y=round(new_y, 3),
    vx=round(new_vx, 3),
    vy=round(new_vy, 3),
  )