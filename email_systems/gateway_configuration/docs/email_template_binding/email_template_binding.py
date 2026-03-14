"""Doc runtime hooks for email_template_binding."""

class DocRuntime:
    doc_key = "email_template_binding"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'activate', 'archive']
