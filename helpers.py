"""helper functions for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import base64
import mimetypes
import os
import urllib
import webbrowser

from adal import AuthenticationContext
import pyperclip
import requests
import os

import config

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "RefreshToken.txt"
RefreshTokenFile = os.path.join(script_dir, rel_path)

def api_endpoint(url):
    """Convert a relative path such as /me/photo/$value to a full URI based
    on the current RESOURCE and API_VERSION settings in config.py.
    """
    if urllib.parse.urlparse(url).scheme in ['http', 'https']:
        return url # url is already complete
    return urllib.parse.urljoin(f'{config.RESOURCE}/{config.API_VERSION}/',
                                url.lstrip('/'))

def get_access_token(client_id):
    with open(RefreshTokenFile, 'r') as file:
        RefreshToken = file.read().replace('\n', '')
    
    if not RefreshToken:
        session = device_flow_session(config.CLIENT_ID, True)
        return session
    else:
        ctx = AuthenticationContext(config.AUTHORITY_URL, api_version=None)
        try:
            token_response = ctx.acquire_token_with_refresh_token(RefreshToken, client_id, config.RESOURCE)
        except:
            session = device_flow_session(config.CLIENT_ID, True)
            return session
        if not token_response.get('accessToken', None):
            session = device_flow_session(config.CLIENT_ID, True)
            return session
        else:
            session = requests.Session()
            session.headers.update({'Authorization': f'Bearer {token_response["accessToken"]}',
                                'SdkVersion': 'sample-python-adal',
                                'x-client-SKU': 'sample-python-adal'})
            return session
    

def device_flow_session(client_id, auto=False):
    """Obtain an access token from Azure AD (via device flow) and create
    a Requests session instance ready to make authenticated calls to
    Microsoft Graph.

    client_id = Application ID for registered "Azure AD only" V1-endpoint app
    auto      = whether to copy device code to clipboard and auto-launch browser

    Returns Requests session object if user signed in successfully. The session
    includes the access token in an Authorization header.

    User identity must be an organizational account (ADAL does not support MSAs).
    """
    ctx = AuthenticationContext(config.AUTHORITY_URL, api_version=None)
    device_code = ctx.acquire_user_code(config.RESOURCE,
                                        client_id)

    # display user instructions
    if auto:
        pyperclip.copy(device_code['user_code']) # copy user code to clipboard
        webbrowser.open(device_code['verification_url']) # open browser
        print(f'The code {device_code["user_code"]} has been copied to your clipboard, '
              f'and your web browser is opening {device_code["verification_url"]}. '
              'Paste the code to sign in.')
    else:
        print(device_code['message'])

    token_response = ctx.acquire_token_with_device_code(config.RESOURCE,
                                                        device_code,
                                                        client_id)
    if not token_response.get('accessToken', None):
        return None
    
    with open(RefreshTokenFile, "w") as RefreshToken:
        RefreshToken.write(token_response["refreshToken"])

    RefreshToken = token_response["refreshToken"]

    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token_response["accessToken"]}',
                            'SdkVersion': 'sample-python-adal',
                            'x-client-SKU': 'sample-python-adal'})
    return session
