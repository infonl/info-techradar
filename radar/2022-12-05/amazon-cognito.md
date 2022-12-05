---
title: "Amazon Cognito"
ring: adopt
quadrant: platforms
featured: true
---

In the space of Identity and Access Management (IAM) we prefer to use <a href="https://aws.amazon.com/cognito/">Amazon Cognito</a> for Customer Identity and Access Management. Cognito may be combined with <a href="aws-iam.html">AWS IAM</a> depending on your needs. Cognito provides amongst others user sign-up, sign-in and access control features while AWS IAM is more low-level focussing on AWS account and permission management.

When using Cognito strongly consider to also use the <a href="https://www.npmjs.com/package/@aws-amplify/ui-react">Amplify UI React</a> UI library which provides out-of-the-box UI components for Cognito authentication workflows.

We are also trialling the SaaS IAM service <a href="clerk.html">Clerk</a> as an potential alternative solution for projects which are not using AWS as the main platform (but typically use a PaaS provider instead).

