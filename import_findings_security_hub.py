from imp import source_from_cache
import os
import json
import logging
import boto3
import securityhub
from datetime import datetime, timezone

FINDING_TITLE = "CodeAnalysis"
account_id = "449630918120"
region = "us-west-2"
source_repository = "ASE-ZAP-Security-Hub"
source_branch = "main"
source_commitid = "1"
build_id = "1"
report_url = "https://aws.amazon.com"
report_type = "OWASP-Zap code scan"
generator_id = f"{report_type.lower()}-{source_repository}-{source_branch}"
finding_type = "OWASP-Zap code scan"
report_type = "OWASP-Zap"
BEST_PRACTICES_OWASP = "https://owasp.org/www-project-top-ten/"

def import_findings_security_hub(event):
    severity = 50
    alert_ct = event['report']['site'][0]['alerts']
    alert_count = len(alert_ct)
    for alertno in range(alert_count):
        risk_desc = event['report']['site'][0]['alerts'][alertno]['riskdesc']
        riskletters = risk_desc[0:3]
        if riskletters == 'Hig':
            normalized_severity = 70
        elif riskletters == 'Med':
            normalized_severity = 60
        elif riskletters == 'Low' or riskletters == 'Inf':  
            normalized_severity = 30
        else:
            normalized_severity = 90                                       
        instances = len(event['report']['site'][0]['alerts'][alertno]['instances'])
        finding_description = f"{alertno}-Vulerability:{event['report']['site'][0]['alerts'][alertno]['alert']}-Total occurances of this issue:{instances}"
        finding_id = f"{alertno}-{report_type.lower()}-{build_id}"
        created_at = datetime.now(timezone.utc).isoformat()
        ### Calling Securityhub function to post the findings
        securityhub.import_finding_to_sh(alertno, account_id, region, created_at, source_repository, source_branch, source_commitid, build_id, report_url, finding_id, generator_id, normalized_severity, severity, finding_type, FINDING_TITLE, finding_description, BEST_PRACTICES_OWASP)

import_findings_security_hub("/zap_results/VulFlask_parametrized_zap_scan.json")
