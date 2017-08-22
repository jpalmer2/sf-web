CASE_ATTRS = ['Id', 'Subject', 'Severity_Level__c', 'CaseNumber', 'AccountId', 'OwnerId', 'CreatedDate', 'CreatedById', 'LastModifiedDate', 'URL_for_Support__c','Owner.Name', 'Owner.Type', 'Owner.Id']

from datetime import datetime
from dateutil import tz

"""
def query_cases_by_statuses(sf, status=['New','Open']):


    Query Salesforce for any New or Open cases
    
    Return a list of cases
    
    Accepts a SalesForce connection object


    where_list = map(lambda x: "Status = '{}'".format(x), status)

    sf_query = ["SELECT",
                ", ".join(CASE_ATTRS),
                "FROM Case WHERE",
                " OR ".join(where_list)]

    results = sf.query(" ".join(sf_query))
    return results['records']

def query_case_by_status(sf, status):
    return query_case_by_status(sf, [status])
"""

def where_or(query_object, object_attrs, match_field, match_values):
    where_list = map(lambda x: "{} = '{}'".format(match_field, x), match_values)

    sf_query = ["SELECT",
                ", ".join(object_attrs),
                "FROM {} WHERE".format(query_object),
                " OR ".join(where_list)]

    query_string = " ".join(sf_query)
    return query_string

def case_new_open(case_attrs=CASE_ATTRS):
    return where_or('Case', case_attrs, 'Status', ['New', 'Open'])

def case_by_status(statuses, case_attrs=CASE_ATTRS):
    return where_or('Case', case_attrs, 'Status', statuses)
