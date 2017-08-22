def get_token():
    from simple_salesforce import Salesforce

    sf=Salesforce(**cred())
    return 'Bearer {}'.format(sf.session_id)

def cred():
    import os

    conf_keys = {'SF_USERNAME': 'username',
                 'SF_PASSWORD': 'password',
                 'SF_SECURITY_TOKEN': 'security_token',
                 'SF_INSTANCE_URL': 'instance_url'}
    
    conf = os.environ

    conf_available = reduce(lambda x, y: x and y,
                            [ x in conf for x in conf_keys],
                            True)
    if conf_available == False:
        raise ValueError("Environment Variable Missing")
    return dict([(v,conf[k]) for k, v in conf_keys.items()])
        
