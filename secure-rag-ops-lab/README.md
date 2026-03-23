# secure-rag-ops-lab

権限制御、出典表示、品質評価を重視したRAG検証プロジェクトです。

## Goal
- 文書検索と回答生成を分離して設計する
- 権限制御を入れる
- 出典付き回答を返す
- 品質評価をスクリプト化する

## Planned Structure
- `src/ingest.py`
- `src/retrieval.py`
- `src/access_control.py`
- `src/evaluation.py`
- `tests/`

## Planned Features
- Chunking
- Embedding
- Retrieval
- Citation output
- Access control
- Offline evaluation