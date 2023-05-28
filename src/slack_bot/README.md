# Slack Bot Setup Guide
This document provides clear instructions for setting up and running your Slack Bot. Please follow these steps carefully:

1. Access the Slack App Settings: Navigate to the following URL: https://api.slack.com/apps/A0561ETAQPR/oauth?

2. Install the App into your workspace:
   - If the App is already installed, please proceed to step 3.

3. Generate Bot User OAuth Token: This token is necessary for allowing the bot to interact with your workspace.

4. Generate App Token:

   - Go to the following URL: https://api.slack.com/apps/A0561ETAQPR/general?
   - Here, generate the App-Level Token.
   - The necessary scopes for the App-Level Token are connections:write and authorizations:read.
5. Update .env file: Insert both the Bot User OAuth Token and the App-Level Token into your .env file. This will allow your script to authenticate with Slack's API.

6. Run Slack Bot: Finally, initiate the Slack Bot by running the slack_bot.py script.

By adhering to these steps, you should be able to successfully set up and run your Slack Bot. If you encounter any issues, please refer to the troubleshooting section or reach out for assistance.