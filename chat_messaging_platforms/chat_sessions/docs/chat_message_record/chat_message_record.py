"""Doc runtime hooks for chat_message_record."""

class DocRuntime:
    doc_key = "chat_message_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'send', 'deliver', 'fail', 'archive']
