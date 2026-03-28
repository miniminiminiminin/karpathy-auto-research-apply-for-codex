import argparse
import asyncio
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

from codex_writer.api.generate import generate_batch, generate_pipeline
from codex_writer.control.uds import DaemonClient
from codex_writer.daemon.server import DaemonServer
from codex_writer.input.load import load_items
from codex_writer.pipeline.load import load_pipeline
from codex_writer.validate import ValidationSpec, validate_file
from codex_writer.workspace.init import initialize_workspace


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="codex-writer")
    subparsers = parser.add_subparsers(dest="command", required=True)
    _add_generate(subparsers)
    _add_validate(subparsers)
    _add_daemon(subparsers)
    _add_job(subparsers)
    _add_workspace(subparsers)
    _add_pipeline(subparsers)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "generate":
        items = load_items(Path(args.input))
        result = generate_batch(
            args.prompt_template,
            items,
            Path(args.output_dir),
            Path(args.runtime_dir),
            concurrency=args.concurrency,
            dry_run=args.dry_run,
        )
        print(json.dumps(asdict(result), ensure_ascii=True))
        return 0
    if args.command == "workspace" and args.workspace_command == "init":
        initialize_workspace(Path(args.workspace), args.preset)
        return 0
    if args.command == "pipeline" and args.pipeline_command == "run":
        result = generate_pipeline(
            pipeline=Path(args.pipeline),
            manifest=Path(args.manifest),
            output_dir=Path(args.output_dir),
            runtime_dir=Path(args.runtime_dir),
            concurrency=args.concurrency,
            dry_run=args.dry_run,
        )
        print(json.dumps(asdict(result), ensure_ascii=True))
        return 0
    if args.command == "validate":
        result = validate_file(
            Path(args.path),
            ValidationSpec(args.min_chars, args.max_chars, tuple(args.require), tuple(args.forbid), args.expect_xml),
        )
        print(json.dumps(_validation_payload(result), ensure_ascii=True))
        return 0 if result.valid else 1
    if args.command == "daemon" and args.daemon_command == "start":
        run_daemon(Path(args.runtime_dir), Path(args.socket_path))
        return 0
    client = DaemonClient(Path(args.socket_path))
    payload = _job_payload(args)
    print(json.dumps(client.request(args.job_command, payload), ensure_ascii=True))
    return 0


def _add_generate(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("generate")
    parser.add_argument("--input", default="items.jsonl")
    parser.add_argument("--prompt-template", default="")
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--runtime-dir", default="runtime")
    parser.add_argument("--concurrency", type=int)
    parser.add_argument("--dry-run", action="store_true")


def _add_validate(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("validate")
    parser.add_argument("path")
    parser.add_argument("--min-chars", type=int)
    parser.add_argument("--max-chars", type=int)
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--expect-xml", action="store_true")


def _add_daemon(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("daemon")
    parser.add_argument("--runtime-dir", default="runtime")
    parser.add_argument("--socket-path", default="runtime/daemon.sock")
    daemon_subparsers = parser.add_subparsers(dest="daemon_command", required=True)
    daemon_subparsers.add_parser("start")


def _add_job(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("job")
    parser.add_argument("--socket-path", default="runtime/daemon.sock")
    job_subparsers = parser.add_subparsers(dest="job_command", required=True)
    submit = job_subparsers.add_parser("submit")
    submit.add_argument("--input", required=True)
    submit.add_argument("--prompt-template")
    submit.add_argument("--pipeline")
    submit.add_argument("--output-dir", required=True)
    submit.add_argument("--concurrency", type=int)
    job_subparsers.add_parser("list")
    for command in ("status", "report", "stop", "resume"):
        command_parser = job_subparsers.add_parser(command)
        command_parser.add_argument("job_id")


def _add_workspace(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("workspace")
    workspace_subparsers = parser.add_subparsers(dest="workspace_command", required=True)
    init = workspace_subparsers.add_parser("init")
    init.add_argument("--workspace", required=True)
    init.add_argument("--preset", default="book-chapter")


def _add_pipeline(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("pipeline")
    pipeline_subparsers = parser.add_subparsers(dest="pipeline_command", required=True)
    run = pipeline_subparsers.add_parser("run")
    run.add_argument("--pipeline", required=True)
    run.add_argument("--manifest", required=True)
    run.add_argument("--output-dir", default="outputs")
    run.add_argument("--runtime-dir", default="runtime")
    run.add_argument("--concurrency", type=int)
    run.add_argument("--dry-run", action="store_true")


def _job_payload(args: argparse.Namespace) -> dict[str, object]:
    if args.job_command == "submit":
        items = [
            {"filename": item.filename, **item.variables}
            for item in load_items(Path(args.input))
        ]
        payload = {
            "prompt_template": args.prompt_template,
            "items": items,
            "output_dir": args.output_dir,
            "concurrency": args.concurrency,
        }
        if args.pipeline:
            payload["pipeline"] = load_pipeline(Path(args.pipeline)).to_dict()
        return payload
    if args.job_command in {"status", "report", "stop", "resume"}:
        return {"job_id": args.job_id}
    return {}


def run_daemon(runtime_dir: Path, socket_path: Path) -> None:
    server = DaemonServer(runtime_dir, socket_path)
    try:
        asyncio.run(_serve_daemon(server))
    except KeyboardInterrupt:
        pass


async def _serve_daemon(server: DaemonServer) -> None:
    await server.start()
    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await server.stop()


def _validation_payload(result: object) -> dict[str, object]:
    if is_dataclass(result):
        raw = asdict(result)
        raw["path"] = str(raw["path"]) if raw.get("path") else None
        return raw
    return {
        "valid": bool(getattr(result, "valid", False)),
        "char_count": int(getattr(result, "char_count", 0)),
        "issues": list(getattr(result, "issues", [])),
        "path": str(getattr(result, "path", "")) or None,
    }
