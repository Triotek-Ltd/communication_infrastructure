"""Doc runtime hooks for email_message_record."""

class DocRuntime:
    doc_key = "email_message_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'queue', 'send', 'retry', 'fail', 'archive']
