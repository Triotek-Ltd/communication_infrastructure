"""Action handler seed for chat_message_record:deliver."""

from __future__ import annotations


DOC_ID = "chat_message_record"
ACTION_ID = "deliver"
ACTION_RULE = {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {}

def handle_deliver(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
