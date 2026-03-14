"""Report-service seed for chat_session_record."""

from __future__ import annotations


DOC_ID = "chat_session_record"
DOC_KIND = "workflow_case"

LIST_COLUMNS = ['title', 'reference_no', 'workflow_state', 'modified']

class ReportService:
    def supports_reporting_hooks(self) -> bool:
        return DOC_KIND in {"transaction", "ledger", "workflow_case"}

    def default_dimensions(self) -> list[str]:
        return LIST_COLUMNS

    def reporting_profile(self) -> dict:
        return {'supports_snapshots': True, 'supports_outputs': False}
