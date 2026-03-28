# Delivery Checklist

- External workspace path is explicit
- Workspace contains prompts, pipelines, manifests, shared, outputs, runtime, scripts, and sdk
- Prompt files are editable in the workspace, not hidden in `.codex`
- Pipeline JSON names all stages and output files
- Manifest rows define one unit each
- Vendored SDK is the actual execution engine
- Direct run command works from the workspace
- Daemon path is documented when interruption matters
- Failed units can be retried without rerunning the full set
- Verification checks both counts and representative output files
