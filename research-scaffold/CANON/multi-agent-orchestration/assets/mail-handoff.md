# Mail Handoff

```text
THREAD := {
  thread_id,
  subject,
  sender_role,
  receiver_role,
  decision_owner,
  verification_owner
}

REQUEST := {
  request_message_id,
  request_status,
  request_artifacts,
  completion_criteria
}

RESPONSE := {
  response_message_id,
  response_status,
  response_artifacts,
  blockers
}

GOVERNANCE := {
  rollback_owner,
  approvals_completed
}

PASS IF
  THREAD.thread_id
  AND REQUEST.completion_criteria
  AND RESPONSE.response_status

FAIL IF
  RESPONSE.blockers_hidden = TRUE
  OR GOVERNANCE.approvals_completed IS implicit
```
