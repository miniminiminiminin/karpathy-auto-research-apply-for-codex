from codex_writer.control.uds import encode_request


def test_encode_request_serializes_command() -> None:
    payload = encode_request("status", {"job_id": "job-1"})
    assert b'"command": "status"' in payload
