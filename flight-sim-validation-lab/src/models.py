from dataclasses import dataclass

@dataclass
class State:
  t: float
  x: float
  y: float
  vx: float
  vy: float


@dataclass
class ObservedState:
  t: float
  x: float
  y: float
  