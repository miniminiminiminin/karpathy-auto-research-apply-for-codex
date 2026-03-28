import json
from pathlib import Path

from codex_writer.jobs.model import JobItem
from codex_writer.output.write import resolve_pipeline_final_path, write_result, write_stage_result
from codex_writer.pipeline.model import PipelineRunResult, PipelineSpec
from codex_writer.template.render import render_prompt


async def run_pipeline_for_item(
    pipeline: PipelineSpec,
    item: JobItem,
    output_dir: Path,
    client: object,
) -> PipelineRunResult:
    previous_output = ""
    stage_paths: list[Path] = []
    tokens_used = 0

    for stage in pipeline.stages:
        prompt_template = stage.prompt_path.read_text(encoding="utf-8")
        prompt = render_prompt(prompt_template, _prompt_variables(item, previous_output))
        result = prompt if getattr(client, "dry_run", False) else await client.generate(prompt)
        body = result if isinstance(result, str) else result.text
        tokens_used += 0 if isinstance(result, str) else result.tokens_used
        stage_path = write_stage_result(output_dir, item.filename, pipeline.final_output, stage.output_file, body)
        stage_paths.append(stage_path)
        previous_output = body

    final_relative = resolve_pipeline_final_path(item.filename, pipeline.final_output)
    final_path = write_result(output_dir, str(final_relative), previous_output)
    return PipelineRunResult(final_path=final_path, stage_paths=stage_paths, tokens_used=tokens_used)


def _prompt_variables(item: JobItem, previous_output: str) -> dict[str, object]:
    payload = {"filename": item.filename, **item.variables}
    return payload | {
        "previous_output": previous_output,
        "item_json": json.dumps(payload, ensure_ascii=False, indent=2),
    }
