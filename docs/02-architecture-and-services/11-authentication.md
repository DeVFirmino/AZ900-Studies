# Authentication: SSO, MFA, passwordless, and Conditional Access

Authentication answers **who you are**. Authorization, covered in the next lesson, answers **what you are allowed to do**.

## Core authentication concepts

| Concept | Meaning | Exam clue |
|---|---|---|
| Authentication | Verify identity, such as with a password, certificate, or token | Sign-in |
| Single sign-on (SSO) | Sign in once and access multiple applications without re-entering credentials | One login for many apps |
| Multi-factor authentication (MFA) | Requires two or more verification methods | Password plus phone, authenticator app, or FIDO key |
| Passwordless | Replace passwords with stronger factors such as FIDO2 keys or the Microsoft Authenticator app | No password in the primary flow |
| External identities | Guest users or partners from other organizations | B2B collaboration |
| Conditional Access | Policy engine that allows, blocks, or requires extra steps based on signals | Require MFA when sign-in is risky or from outside the corporate network |

## Single sign-on (SSO)

SSO improves user experience and reduces password fatigue by federating or synchronizing identity to multiple applications.

**Exam clue:** one corporate login for Azure, Microsoft 365, and SaaS apps → **SSO with Microsoft Entra ID**.

## Multi-factor authentication (MFA)

MFA adds a second factor beyond something you know, such as:

- something you have (phone, token, or authenticator app);
- something you are (biometric verification on supported devices).

**Exam rule:** reduce account takeover risk → **MFA**.

## Passwordless authentication

Passwordless methods reduce phishing and password reuse risks. Examples include FIDO2 security keys and passwordless phone sign-in.

Passwordless is not the same as "no authentication." It replaces the password with stronger verification.

## External identities

Microsoft Entra B2B collaboration lets external users from other tenants or identity providers access your applications and resources as guests.

**Exam clue:** partner vendor needs access to a shared app without creating a duplicate account in your HR system → **external identity / B2B guest**.

## Conditional Access

Conditional Access policies evaluate signals such as user, location, device state, application, and risk level, then enforce requirements such as:

- require MFA;
- block legacy authentication;
- allow access only from compliant devices;
- require an approved client app.

Conditional Access is the **if/then engine** for sign-in and session control.

Example policy logic:

```text
IF user is admin AND sign-in is from an unknown location
THEN require MFA AND block legacy auth clients
```

## Scenario

Remote workers must use an authenticator app in addition to a password when signing in from outside the office network.

**Best fit:** **Conditional Access** requiring **MFA** based on location.

## Scenario

Executives want to sign in to Microsoft 365 and a custom app with one set of corporate credentials.

**Best fit:** **SSO** through **Microsoft Entra ID**.

## Exam clues

- Verify identity → authentication, not RBAC.
- Second factor required → **MFA**.
- Policy based on location, device, or risk → **Conditional Access**.
- Guest partner access → **external identities / B2B**.

## Official references

- [What is Conditional Access?](https://learn.microsoft.com/entra/identity/conditional-access/overview)
- [Multifactor authentication in Microsoft Entra ID](https://learn.microsoft.com/entra/identity/authentication/concept-mfa-howitworks)
- [Single sign-on overview](https://learn.microsoft.com/entra/identity/enterprise-apps/what-is-single-sign-on)
