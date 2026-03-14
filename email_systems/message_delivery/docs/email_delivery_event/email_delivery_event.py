"""Doc runtime hooks for email_delivery_event."""

class DocRuntime:
    doc_key = "email_delivery_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
