# Python Teams Presence Reader

![language:Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square) ![license:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square) 

This sample uses Microsoft Graph to read your user Teams presence status.

This is based on the [Python console application for Microsoft Graph Sample](https://docs.microsoft.com/en-us/samples/microsoftgraph/python-sample-console-app/python-console-application-for-microsoft-graph/) and [microsoft-authentication-library-for-python](https://github.com/AzureAD/microsoft-authentication-library-for-python/blob/dev/sample/device_flow_sample.py)

Authentication is handled via [device flow authentication](#device-flow-authentication), the recommended approach for console applications. If you're looking for examples of how to work with Microsoft Graph from Python _web applications_, see [Python authentication samples for Microsoft Graph](https://github.com/microsoftgraph/python-sample-auth). 

* [Installation](#installation)
* [Running the sample](#running-the-sample)
* [Device Flow authentication](#device-flow-authentication)
* [Helper functions](#helper-functions)
* [Contributing](#contributing)
* [Resources](#resources)

## Installation

Verify that you have the following prerequisites in place before installing the sample:

* Install Python from [https://www.python.org/](https://www.python.org/). You'll need Python 3.6 or later, primarily because of the use of [f-strings](https://www.python.org/dev/peps/pep-0498/) &mdash change those to [format strings](https://docs.python.org/3/library/stdtypes.html#str.format) if you need to use an earlier Python 3.x version. If your code base is running under Python 2.7, you may find it helpful to use the [3to2](https://pypi.python.org/pypi/3to2) tools to port the code to Python 2.7.
* The sample can be run on any operating system that supports Python 3.x, including recent versions of Windows, Linux, and Mac OS. In some cases, you may need to use a different command to launch Python &mdash; for example, some Linux distros reserve the command ```python``` for Python 2.7, so you need to use ```python3``` to launch an installed Python 3.x version.
* This sample requires an [Office 365 for business account](https://msdn.microsoft.com/en-us/office/office365/howto/setup-development-environment#bk_Office365Account).
* To register your application in the Azure Portal, you will need an Azure account associated with your Office 365 account. No charges will be incurred for registering your application in the Azure Portal, but you must have an account. If you don't have one, you can sign up for an [Azure Free Account](https://azure.microsoft.com/en-us/free/free-account-faq/).

Follow these steps to install the sample code on your computer:

1. Clone the repo with this command:
    * ```git clone https://github.com/poiriersimon/PythonTeamsPresence.git```

2. Create and activate a virtual environment (optional). If you're new to Python virtual environments, [Miniconda](https://conda.io/miniconda.html) is a great place to start.

3. In the root folder of your cloned repo, install the dependencies for the sample as listed in the ```requirements.txt``` file with this command: ```pip install -r requirements.txt```.

## Application Registration

To run the sample, you will need to register an application and add the registered application's ID to the configuration information in the [config.py](https://github.com/microsoftgraph/python-sample-console-app/blob/master/helpers.py) file. Follow these steps to register and configure your application:

1. Navigate to the [Azure portal > App registrations](https://go.microsoft.com/fwlink/?linkid=2083908) to register your app. Sign in using a work or school account, or a personal Microsoft account.

2. Select **New registration**.

3. When the **Register an application page** appears, set the values as follows:
    1. Set **Name** to `PythonTeamsPresence`.
    2. Set **Supported account types** to **Accounts in any organizational directory and personal Microsoft accounts**.
    3. Leave **Redirect URI** empty.
    4. Choose **Register**.

4. On the **PythonTeamsPresence** overview page, copy and save the value for the **Application (client) ID**. You'll need it later.

5. Select **API permissions**.
   1. Choose the **Add a permission** button and then make sure that the **Microsoft APIs** tab is selected.
   2. In the **Commonly used Microsoft APIs** section, select **Microsoft Graph**, and then select **Delegated permissions**.
   3. Use the **Select permissions** search box to search for the `Presence.Read` permission.
   4. Select the checkbox for each permission as it appears.
      > **NOTE:** Permissions will not remain visible in the list as you select each one.

6. Go to the **Authentication** page. 
    1. Check the box next to `https://login.microsoftonline.com/common/oauth2/nativeclient`.
    2. Find the setting labeled **Default client type** and set it to `Yes`.
    3. Select **Save** at the top of the page.

After registering your application, modify the ```config.py``` file in the root folder of your cloned repo, and follow the instructions to enter your Client ID (the Application ID value you copied in Step 3 earlier). Save the change, and you're ready to run the sample.

## Running the sample

Follow these steps to run the sample app:

1. At the command prompt, run the command ```python Presence.py```. You'll see a message telling you to open a page in your browser and enter a code.


2. After entering the code at https://aka.ms/devicelogin, you'll be prompted to select an identity or enter an email address to identify yourself. The identity you use must be in the same organization/tenant where the application was registered. Sign in, and then you'll be asked to consent to the application's delegated permissions as shown below. Choose **Accept**.

3. After consenting to permissions, you'll see a message giving your Presence and Activity

## Helper functions

Several helper functions in [helpers.py](https://github.com/microsoftgraph/python-sample-console-app/blob/master/helpers.py) provide simple wrappers for common Graph operations, and provide examples of how to make authenticated Graph requests via the methods of the session object. These helper functions can be used with any auth library &mdash; the only requirement is that the session object has a valid Graph access token stored in its ```Authorization``` header.

### A note on HTTP headers

In this sample, the session object sends the required ```Authorization``` header (which contains the access token) as well as optional headers to identify the libraries used. These headers are set [during the authentication process](https://github.com/microsoftgraph/python-sample-console-app/blob/master/helpers.py#L59-L61). In addition, you may want to create other headers for certain Graph calls. You can do this by passing a ```headers``` dictionary to the Graph call, and this dictionary will be merged with the default headers on the session object. You can see an example of this technique in  parameter for any of the ```send_mail``` helper function, which adds a ```Content-Type``` header as shown [here](https://github.com/microsoftgraph/python-sample-console-app/blob/master/helpers.py#L138-L138).

### api_endpoint(url)

Converts a relative path such as ```/me/photo/$value``` to a full URI based on the current RESOURCE and API_VERSION settings in config.py.

### get_access_token(client_id)

Obtain the Access Token by leveraging the Refresh Token is present and valide, else leverage the device_flow_session to get a new one

## Contributing

These samples are open source, released under the [MIT License](https://github.com/microsoftgraph/python-sample-console-app/blob/master/LICENSE). Issues (including feature requests and/or questions about this sample) and [pull requests](https://github.com/microsoftgraph/python-sample-console-app/pulls) are welcome. If there's another Python sample you'd like to see for Microsoft Graph, we're interested in that feedback as well &mdash; please log an [issue](https://github.com/microsoftgraph/python-sample-console-app/issues) and let us know!

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Resources

* Authentication:
    * [Microsoft ADAL for Python](https://github.com/AzureAD/azure-activedirectory-library-for-python)
    * [Python authentication samples for Microsoft Graph](https://github.com/microsoftgraph/python-sample-auth)
    * [OAuth 2.0 Device Flow for Browserless and Input Constrained Devices](https://tools.ietf.org/html/draft-ietf-oauth-device-flow-07)
* Graph API documentation:
    * [Get a user](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/api/user_get)
    * [Get photo](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/api/profilephoto_get)
    * [Upload or replace the contents of a DriveItem](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/api/driveitem_put_content)
    * [Create a sharing link for a DriveItem](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/api/driveitem_createlink)
    * [Send mail](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/api/user_sendmail)
* Other Python samples for Microsoft Graph:
    * [Sending mail via Microsoft Graph from Python](https://github.com/microsoftgraph/python-sample-send-mail) (web app)
    * [Working with paginated Microsoft Graph responses in Python](https://github.com/microsoftgraph/python-sample-pagination)
    * [Working with Graph open extensions in Python](https://github.com/microsoftgraph/python-sample-open-extensions)
