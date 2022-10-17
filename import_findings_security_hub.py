import os
import json
import logging
import codecs
import datetime
from datetime import datetime, timezone

FINDING_TITLE = "CodeAnalysis"
account_id = "449630918120"
region = "us-west-2"
source_repository = "ASE-ZAP-Security-Hub"
source_branch = "main"
source_commitid = "1"
build_id = "VulFlask ZAP Scan"
report_url = "https://aws.amazon.com"
report_type = "OWASP-Zap code scan"
#generator_id = f"{report_type.lower()}-{source_repository}-{source_branch}"
generator_id = "{0}-{1}-{2}".format(report_type.lower(),source_repository,source_branch)
finding_type = "OWASP-Zap code scan"
report_type = "OWASPZap"
BEST_PRACTICES_OWASP = "https://owasp.org/www-project-top-ten/"
created_at = datetime.now(timezone.utc).isoformat()

zap_aws_sechub_data = []

def import_findings_security_hub(json_file):
    with codecs.open(json_file,'r',encoding='utf-8') as fp:
        datafile = json.load(fp)
        severity = 50
        alerts = datafile['Report']['Sites']
        alertno = 1
        for alert in alerts:
            risk_desc = alert['Alerts']['AlertItem']['RiskDesc']
            if risk_desc == 'High':
                normalized_severity = 70
            elif risk_desc == 'Medium':
                normalized_severity = 60
            elif risk_desc == 'Low' or riskletters == 'Inf':  
                normalized_severity = 30
            else:
                normalized_severity = 90
            Description = alert['Alerts']['AlertItem']['Desc']
            Solution = alert['Alerts']['AlertItem']['Solution']
            Title = alert['Alerts']['AlertItem']['Alert']
            CWEID = alert['Alerts']['AlertItem']['CWEID'] or 0

            #finding_id = f"{alertno}{report_type.lower()}"
            finding_id = "{0}{1}".format(alertno,report_type.lower())
            
            int_data = {
                "SchemaVersion": "2018-10-08",
                "Id": finding_id,
                "ProductArn": "arn:aws:securityhub:{0}:{1}:product/{1}/default".format(region, account_id),
                "GeneratorId": generator_id,
                "AwsAccountId": account_id,
                "Types": [
                    "Software and Configuration Checks/AWS Security Best Practices/{0}".format(
                        finding_type)
                ],
                "CreatedAt": created_at,
                "UpdatedAt": created_at,
                "Severity": {
                    "Normalized": normalized_severity,
                },
                "Title":  Title,
                "Description": Description,
                'Remediation': {
                    'Recommendation': {
                        'Text': Solution,
                        'Url': 'https://cwe.mitre.org/data/definitions/%s.html'%CWEID
                    }
                },
                'SourceUrl': 'https://cwe.mitre.org/data/definitions/%s.html'%CWEID,
                'Resources': [
                    {
                        'Id': build_id,
                        'Type': "ZAP",
                        'Partition': "aws",
                        'Region': region
                    }
                ],
            }
            zap_aws_sechub_data.append(int_data)
            alertno = alertno + 1
            
    with open('/zap_results/zap_aws_sechub_data.json', 'w') as fp:
        json.dump(zap_aws_sechub_data,fp)

import_findings_security_hub("/zap_results/VulFlask_parametrized_zap_scan.json")
