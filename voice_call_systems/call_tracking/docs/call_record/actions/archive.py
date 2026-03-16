"""Action handler seed for call_record:archive."""

from __future__ import annotations


DOC_ID = "call_record"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['initiated', 'ringing', 'answered', 'missed', 'failed', 'completed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['voice_provider', 'call_event_log', 'service_case'], 'borrowed_fields': ['provider', 'number context from voice_provider'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
