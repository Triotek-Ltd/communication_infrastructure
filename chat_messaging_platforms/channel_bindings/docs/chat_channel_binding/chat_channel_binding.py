"""Doc runtime hooks for chat_channel_binding."""

class DocRuntime:
    doc_key = "chat_channel_binding"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
