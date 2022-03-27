# Authentication Eguna

## Intro

Authentication is the act of proving an assertion, such as the **identity** of a computer system user. **Authentication is the process of verifying identity**. It might involve validating personal identity documents or verifying the authenticity of a website.

In computer systems, verifying a user's identity is often required to allow access to confidential data or systems.


### Authentication factors

The way someone may be authentificated fall into three categories based in the following factors: something the *user* knows, something that he user *has*, and something that the user *is*. Preferably all three, or at least two, factor should be verified.

- **Knowledge factors**: Something that the user knows. E.g., password, PIN, challenge response, security question.

- **Ownership factors**: Something that the user *has*. E.g., security token, ID card.

- **Inference factors**: Something that the user *is*. Eg.g, fingerprint, retinal pattern, DNA sequence, signature, voice.

### Authentication types

The authentication types differ in the level of security provided.

- **Strong authentication**: Layered authentication approach relying on two or more authenticators. The factors that are used must be mutually independent, and at least one must be non-replicable. 

- **Continuous authentication**: Conventional computer systems authenticate users only at the initial log-in session, which can be the cause of a critical security flaw. To resolve this problem, systems need continuous user authentication methods that continuously monitor and authenticate users based on some biometric trait(s). A study used behavioural biometrics based in writing styles as a continuous authentication method.

- **Digital authentication**: Processes where the user identification is established via electronic methods. 

- **Product authentication**: Efforts to control the supply chain and educate consumers help ensure that authentic products are sold and used.

## User authentication

In this repository we will focus on **user authentication**, a very common process that covers all of the human-computer interactions that require the user to login. Authentication asks each user, "who are you?" and verifies their response. It has three main tasks:

1. Manage the connection between the user and the webstire's server
2. Verify user's identities
3. Approve or decline the user

There are different authentication protocols: *Password Authentication Protocol* (PAP), cookie-based authentication, token-based authentication...

## Password Authentication Protocol

It is very simple: 1. User sends username and password 2.Server sends an authentication-ack or authentication-nak.

See `/password_authentication_protocol` for PAP in Django. 
