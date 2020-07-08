# -*- coding: utf-8 -*-
##########################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2017-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
##########################################################################


{
    "name":  "MSG91 SMS Gateway",
    "summary":  "Send sms notifications using Msg91 SMS gateway.",
    "category":  "Marketing",
    "version":  "1.0.1",
    "sequence":  1,
    "author":  "Webkul Software Pvt. Ltd.",
    "license":  "Other proprietary",
    "website":  "http://www.webkul.com",
    "description":  """This MSG91 sms gateway is used to send the sms to the mobile numbers.""",
    "live_test_url":  "http://odoodemo.webkul.com/?module=msg91_gateway&version=11.0",
    "depends":  ['sms_notification'],
    "data":  [
        'views/msg91_config_view.xml',
        'views/sms_report.xml',
    ],
    "images":  ['static/description/Banner.png'],
    "application":  True,
    "installable":  True,
    "auto_install":  False,
    "price":  20,
    "currency":  "EUR",
    "pre_init_hook":  "pre_init_check",
}
