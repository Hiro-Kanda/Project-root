# flight-sim-validation-lab

2D飛行体の簡易シミュレーションと解析・検証を行うプロジェクトです。

## Goal
- 2D飛行モデルを実装する
- ノイズと擾乱を加える
- 軌道を比較する
- 条件差分の検証を行う
- 結果をレポート化する

## Planned Structure
- `src/dynamics.py`
- `src/simulator.py`
- `src/validator.py`
- `notebooks/`
- `tests/`

## Planned Features
- Position/velocity update
- Wind disturbance
- Sensor noise
- Monte Carlo runs
- Validation metrics
- Report generation