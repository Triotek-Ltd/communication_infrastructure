"""Action handler seed for email_delivery_event:record."""

from __future__ import annotations


DOC_ID = "email_delivery_event"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['email_message_record', 'email_gateway'], 'borrowed_fields': ['provider/message context from linked records'], 'inferred_roles': ['operations coordinator']}, 'actors': ['operations coordinator'], 'action_actors': {'record': ['operations coordinator'], 'archive': ['operations coordinator']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
