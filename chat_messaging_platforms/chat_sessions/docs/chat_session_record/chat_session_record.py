"""Doc runtime hooks for chat_session_record."""

class DocRuntime:
    doc_key = "chat_session_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'reply', 'close', 'reopen', 'archive']
