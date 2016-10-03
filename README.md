# communication-service
The service that handles all E-mail and SMS based communication for different services in the PEC ecosystem.

### Features
This service provides the following features for any client/service calling it:

1. Sending email and SMSes to single/multiple users at a time with a single API call.
2. Access history of sent emails/SMSes by that particular service.
3. Ability of track message events for emails, that is, whether the message was accepted, rejected, failed, delivered, etc.
4. Schedule email/SMS to be sent at some later time.

### Implementation
This service shall use the services of Mailgun for sending emails.

Communication service exposes a set of REST endpoints for carrying out the tasks mentioned above. The core API has been written in Python Flask. The client can use any programming language to call the service.
All requests should be sent over `https`.

### Security
Only services that are explicitly whitelisted by the Communication service are allowed to successfully call the endpoints.
Each calling service must obtain a clientId and client secret key before starting to use it.

Please see the generic services document to get a idea of how security is implemented.

#### How to integrate
Please contact us with the following details:

1. Name of your app/service and its relation to PEC ecosystem.
2. A list of API methods you shall be calling, and the purpose of each method in brief.

We will follow up on the matter with you.

### Help
If you need any assistance, please open an issue on GitHub.
