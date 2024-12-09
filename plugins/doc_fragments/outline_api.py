from __future__ import annotations


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
    api_endpoint:
        description:
            - URL of your Outline instance API (e.g. V(https://app.getoutline.com/api))
            - You can also set this option by using the E(OUTLINE_API_URL) environment variable
        required: true
        type: str
    api_token:
        description:
            - API Token
            - You can also set this option by using the E(OUTLINE_API_TOKEN) environment variable
        required: true
        type: str
"""
