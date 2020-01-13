#!/usr/bin/env bash
export CAS_CLIENT_SSL_CA_LIST='{path_to_cert}/trustedcerts.pem'
source {path_to_code}/venv/bin/activate
python {path_to_code}/app.py --report MarketingProducts
