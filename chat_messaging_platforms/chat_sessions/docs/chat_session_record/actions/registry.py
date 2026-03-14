"""Action registry seed for chat_session_record."""

from __future__ import annotations


DOC_ID = "chat_session_record"
ALLOWED_ACTIONS = ['create', 'assign', 'reply', 'close', 'reopen', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': None}, 'reply': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': 'closed'}, 'reopen': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['open', 'assigned', 'active', 'reopened'], 'transitions_to': 'archived'}}

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
