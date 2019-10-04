class login_info:
    def __init__(self,
                 username,
                 password,
                 login_attempt = 'Log in',
                 token = '+\\',
                 edit_token = '+\\',
                 title = 'Special:UserLogin',
                 auth_action = 'login',
                 force = '',
                 force_https = '1',
                 from_http = '1'):

        self.wpName = username
        self.wpPassword = password
        self.wploginattempt = login_attempt
        self.wpLoginToken = token
        self.wpEditToken = edit_token
        self.title = title
        self.authAction = auth_action
        self.force = force
        self.wpForceHttps = force_https
        self.wpFromhttp = from_http

