"""Action registry seed for chat_message_record."""

from __future__ import annotations


DOC_ID = "chat_message_record"
ALLOWED_ACTIONS = ['create', 'send', 'deliver', 'fail', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': None}, 'send': {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': None}, 'deliver': {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': None}, 'fail': {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['received', 'created', 'sent', 'delivered', 'read', 'failed'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
