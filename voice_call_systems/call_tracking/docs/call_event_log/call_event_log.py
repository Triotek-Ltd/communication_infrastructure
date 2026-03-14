"""Doc runtime hooks for call_event_log."""

class DocRuntime:
    doc_key = "call_event_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
