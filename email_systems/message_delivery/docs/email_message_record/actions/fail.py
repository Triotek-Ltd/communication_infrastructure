"""Action handler seed for email_message_record:fail."""

from __future__ import annotations


DOC_ID = "email_message_record"
ACTION_ID = "fail"
ACTION_RULE = {'allowed_in_states': ['created', 'queued', 'sent', 'delivered', 'bounced', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['email_gateway', 'email_delivery_event', 'email_template_binding', 'correspondence_record'], 'borrowed_fields': ['gateway identity from email_gateway', 'template refs from email_template_binding'], 'inferred_roles': ['operations coordinator']}, 'actors': ['operations coordinator'], 'action_actors': {'create': ['operations coordinator'], 'archive': ['operations coordinator']}}

def handle_fail(payload: dict, context: dict | None = None) -> dict:
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
