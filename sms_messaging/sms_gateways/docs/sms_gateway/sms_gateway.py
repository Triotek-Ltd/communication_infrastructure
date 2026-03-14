"""Doc runtime hooks for sms_gateway."""

class DocRuntime:
    doc_key = "sms_gateway"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
