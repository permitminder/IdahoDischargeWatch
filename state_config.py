"""
State configuration for this IdahoDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "ID"
STATE_NAME = "Idaho"
APP_NAME = "IdahoDischargeWatch"
APP_TAGLINE = "Idaho Discharge Monitoring"
DOMAIN = "idahodischargewatch.org"
DATA_FILE = "id_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@idahodischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "MST"
EPA_REGION = 10
