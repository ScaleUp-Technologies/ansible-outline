# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Moritz Jannasch <mjannasch@scaleuptech.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


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
