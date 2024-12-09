# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Moritz Jannasch <mjannasch@scaleuptech.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, annotations, division, print_function


__metaclass__ = type

argument_spec = dict(
    api_endpoint=dict(type="str", required=True),
    api_token=dict(type="str", required=True, no_log=True),
)
