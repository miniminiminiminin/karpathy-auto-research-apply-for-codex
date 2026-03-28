# Runtime Options

```text
IF batch_size = small OR batch_size = medium
  AND reruns_are_cheap
  AND shortest_path_is_preferred
THEN runtime_mode := direct_pipeline_run

ELSE IF per_item_retry_matters
  OR runtime_artifacts_must_remain_inspectable
THEN runtime_mode := persisted_batch_runner

ELSE IF jobs_are_long_running
  OR stop_resume_is_required
  OR pipeline_execution_must_survive_interruption
THEN runtime_mode := daemon_managed_execution

ELSE
  STOP("runtime mode is still ambiguous")
```
