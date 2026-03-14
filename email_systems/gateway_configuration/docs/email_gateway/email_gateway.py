"""Doc runtime hooks for email_gateway."""

class DocRuntime:
    doc_key = "email_gateway"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
