"""Doc runtime hooks for voice_provider."""

class DocRuntime:
    doc_key = "voice_provider"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
