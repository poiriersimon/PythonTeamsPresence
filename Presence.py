"""Python console app with device flow authentication."""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import pprint

import config

from helpers import api_endpoint, get_access_token

def getpresence(session):
    """Get Presence from loged in user"""
    print('\nGet user profile ---------> https://graph.microsoft.com/beta/me')
    user_profile = session.get(api_endpoint('me'))
    print(28*' ' + f'<Response [{user_profile.status_code}]>', f'bytes returned: {len(user_profile.text)}\n')
    if not user_profile.ok:
        pprint.pprint(user_profile.json()) # display error
        return
    user_data = user_profile.json()
    email = user_data['mail']
    display_name = user_data['displayName']

    
    print(f'Your name ----------------> {display_name}')
    print(f'Your email ---------------> {email}')

    print('\nGet user presence ---------> https://graph.microsoft.com/beta/me/presence')
    user_presence = session.get(api_endpoint('me/presence'))
    print(28*' ' + f'<Response [{user_presence.status_code}]>', f'bytes returned: {len(user_presence.text)}\n')
    if not user_presence.ok:
        pprint.pprint(user_presence.json()) # display error
        return
    user_data = user_presence.json()
    availability = user_data['availability']
    activity = user_data['activity']

    
    print(f'Your availability ----------------> {availability}')
    print(f'Your activity ---------------> {activity}')

if __name__ == '__main__':
    #GRAPH_SESSION = device_flow_session(config.CLIENT_ID, True)
    GRAPH_SESSION = get_access_token(config.CLIENT_ID)
    if GRAPH_SESSION:
        getpresence(GRAPH_SESSION)
