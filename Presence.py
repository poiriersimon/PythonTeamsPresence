"""Python console app with device flow authentication."""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import pprint

import config

from helpers import api_endpoint, get_access_token

def getpresence(session):
    """Get Presence from logged in user"""
    user_profile = session.get(api_endpoint('me'))
   
    if not user_profile.ok:
        pprint.pprint(user_profile.json()) # display error
        return
    user_data = user_profile.json()
    display_name = user_data['displayName']
    
    print(f'Your name ----------------> {display_name}')
    print('\nGet user presence ---------> https://graph.microsoft.com/beta/me/presence')
    user_presence = session.get(api_endpoint('me/presence'))
   
    if not user_presence.ok:
        pprint.pprint(user_presence.json()) # display error
        return
    user_data = user_presence.json()
    availability = user_data['availability']
    activity = user_data['activity']
    
    print(f'Your availability ----------------> {availability}')
    print(f'Your activity ---------------> {activity}')

if __name__ == '__main__':
    GRAPH_SESSION = get_access_token(config.CLIENT_ID)
    if GRAPH_SESSION:
        getpresence(GRAPH_SESSION)
