from __future__ import annotations


argument_spec = dict(
    state=dict(choices=["present", "absent"], default="present"),
    api_endpoint=dict(type="str", required=True),
    api_token=dict(type="str", required=True, no_log=True),
)
