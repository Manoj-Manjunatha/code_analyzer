"""Code Analyzer API."""

from .code_analyze import CodeAnalyze


def configure_api(api_manager):
    """Define all APIs here."""
    api_manager.add_resource(CodeAnalyze,
                             '/api/code-analyze',
                             '/api/code-analyze/')
