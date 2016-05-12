from authomatic.providers import oauth2, oauth1, openid, gaeopenid

CONFIG = {
    
    'tw': { # Your internal provider name
        
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '3mCv2HwSRvsrtd8EfgPaLJyDO',
        'consumer_secret': '7EFE17qxtWWJjU4C8thkfoY2zUJUWSaYulxLH9J6e5EJYJ7L8U',
    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1671667536450384',
        'consumer_secret': '7dcdc9e67fde9f34e4f13767343b59dc',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    
    'oi': {
           
        # OpenID provider dependent on the python-openid package.
        'class_': openid.OpenID,
    }
}
