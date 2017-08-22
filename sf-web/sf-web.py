from flask import Flask
from flask import render_template
import simple_salesforce
import sto_sf
import sto_sf.sf_queries as sf_queries
import sto_sf.util as util
from sto_sf.cred import cred

app = Flask(__name__)

@app.route('/')
def new_open():
    sf=simple_salesforce.Salesforce(**cred())
    fields = ['isMosAlert__c',
              'Milestone_violated__c',
              'First_Reply__c',
              'CaseNumber',
              'Severity_Level__c',
              'Status',
              'Subject',
              'URL_for_support__c']
    quer = sf_queries.case_new_open(fields)
    res = sf.query(quer)['records'] 
    table = { 'headers': fields,
              'rows': res,
              }
    page = { 'title': 'New and Open Cases',
             'header': 'New and Open Cases',
             }
    return render_template('base_table.html.j2', page=page, table=table)


@app.route('/case/<case_num>')
def case_details(case_num):
    if case_num.isdigit() != True: raise ValueError
    sf=simple_salesforce.Salesforce(**cred())
    case_id = sf.query("SELECT Id from Case where CaseNumber = '{}'".format(int(case_num)))['records'][0]['Id']
    res = sf.Case.get(case_id)
    table = { 'headers': [0,1],
              'rows': res.items(),
              }
    page = { 'title': 'Case sobjects - {}'.format(case_num),
             'header': 'Case {}({})'.format(case_num, case_id),
             }
    return render_template('base_table.html.j2', page=page, table=table)             


"""
    for header in table['headers']:
        print "header({})".format(header)
    print "\n".format()

    for row in table['rows']:
        for header in table['headers']:
            if header in row.keys():
                cell = row[header]
            else:
                cell = ''
            print '{}({})'.format(header, cell)
        print "\n".format()
"""
