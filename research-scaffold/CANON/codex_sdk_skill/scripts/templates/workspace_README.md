# Batch Workspace

Edit the files in `prompts/`, `pipelines/`, `manifests/`, and `shared/`, then run:

```bash
PYTHONPATH=sdk/src python scripts/run_pipeline.py \
  --pipeline pipelines/book-chapter.json \
  --manifest manifests/chapters.jsonl
```
