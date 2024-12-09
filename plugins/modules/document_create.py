#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Moritz Jannasch <mjannasch@scaleuptech.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = r"""
---
module: document_create

short_description: Create a document in Outline

version_added: "0.0.1"

description:
    - Create a new document in Outline.
    - By default a document is set to the collection root.
    - If you want to create a nested/child document, you should pass parent_document_id.

extends_documentation_fragment:
    - scaleuptechnologies.outline_api.outline_api

options:
    title:
        description:
            - The title of the document.
        required: true
        type: str
    text:
        description:
            - The body of the document, may contain markdown formatting.
        type: str
        default: ""
    collection_id:
        description:
            - Identifier for the collection to create the document in.
        required: true
        type: str
    parent_document_id:
        description:
            - Identifier for the document this should be a child of.
        type: str
    template_id:
        description:
            - Identifier for the template to create this document from.
        type: str
    template:
        description:
            - Whether this document should be considered to be a template.
        type: bool
        default: false
    publish:
        description:
            - Whether this document should be immediately published
            - and made visible to other team members.
        type: bool
        default: false

author:
    - Moritz Jannasch (@mojansch)
"""

EXAMPLES = r"""
- name: Create a simple document
  scaleuptechnologies.outline_api.document_create:
    api_endpoint: https://outline.example.com/api
    api_token: secret_token
    title: "My Document"
    collection_id: "c99ad6f3-04b8-4181-aa20-5d5670f5f984"
    text: "# Hello World\n\nThis is my document"
    publish: true

- name: Create a document from template
  scaleuptechnologies.outline_api.document_create:
    api_endpoint: https://outline.example.com/api
    api_token: secret_token
    title: "My Document from Template"
    collection_id: "c99ad6f3-04b8-4181-aa20-5d5670f5f984"
    template_id: "bed4fe68-7b0b-496f-988b-ca31333e23fb"
    publish: true

- name: Create a nested document
  scaleuptechnologies.outline_api.document_create:
    api_endpoint: https://outline.example.com/api
    api_token: secret_token
    title: "Child Document"
    collection_id: "c99ad6f3-04b8-4181-aa20-5d5670f5f984"
    parent_document_id: "a79c0232-3d65-43b1-b676-7ecadc57a08f"
    text: "This is a child document"
"""

RETURN = r"""
document:
    description: The created document object
    type: dict
    returned: always
    contains:
        id:
            description: Unique identifier for the document
            type: str
            sample: "a79c0232-3d65-43b1-b676-7ecadc57a08f"
        title:
            description: The title of the document
            type: str
            sample: "My Document"
        text:
            description: The text content of the document
            type: str
            sample: "# Hello World"
        collectionId:
            description: The ID of the collection this document belongs to
            type: str
            sample: "c99ad6f3-04b8-4181-aa20-5d5670f5f984"
        createdAt:
            description: Timestamp when the document was created
            type: str
            sample: "2024-01-20T12:00:00.000Z"
        updatedAt:
            description: Timestamp when the document was last updated
            type: str
            sample: "2024-01-20T12:00:00.000Z"
"""

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

from ..module_utils.base import argument_spec


def run_module():
    module_args = dict(
        title=dict(type="str", required=True),
        text=dict(type="str", default=""),
        collection_id=dict(type="str", required=True),
        parent_document_id=dict(type="str"),
        template_id=dict(type="str"),
        template=dict(type="bool", default=False),
        publish=dict(type="bool", default=False),
    )

    module_args = {**module_args, **argument_spec}

    result = dict(
        changed=False,
        document={},
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.check_mode:
        module.exit_json(**result)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f'Bearer {module.params["api_token"]}',
    }

    payload = {
        "title": module.params["title"],
        "text": module.params["text"],
        "collectionId": module.params["collection_id"],
        "template": module.params["template"],
        "publish": module.params["publish"],
    }

    if module.params["parent_document_id"]:
        payload["parentDocumentId"] = module.params["parent_document_id"]
    if module.params["template_id"]:
        payload["templateId"] = module.params["template_id"]

    url = f"{module.params['api_endpoint']}/documents.create"

    try:
        response, info = fetch_url(
            module,
            url,
            data=json.dumps(payload),
            headers=headers,
            method="POST",
        )

        if info["status"] != 200:
            module.fail_json(
                msg=f"Failed to create document: HTTP {info['status']}",
                http_response=info["body"],
                **result,
            )

        response_data = json.loads(response.read())

        if not response_data.get("data"):
            module.fail_json(msg="Invalid response from API", **result)

        result["document"] = response_data["data"]
        result["changed"] = True

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Error creating document: {str(e)}", **result)


def main():
    run_module()


if __name__ == "__main__":
    main()
