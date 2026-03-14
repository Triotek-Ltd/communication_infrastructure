"""Doc runtime hooks for sms_delivery_event."""

class DocRuntime:
    doc_key = "sms_delivery_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
