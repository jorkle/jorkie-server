# Jorkie Project Document

## What is "Jorkie"?

**Jorkie** is an automated reconnaissance solution for Bug Bounty Hunters. **Jorkie** consists of three components:

1. Jorkie Console
2. Jorkie Agents
3. Jorkie Server

### What is "Jorkie Console"

The Jorkie Console is a web-based application that allows users to manage their Jorkie Agents and view the results of the reconnaissance scans. The Jorkie Console is the main interface for users to interact with the Jorkie system.

### What is "Jorkie Agents"

Jorkie Agents are small dockerized tasks which perform individual reconnaissance tasks. Jorkie Agents are designed to be lightweight and easy to deploy. Jorkie Agents are managed by the Jorkie Server and can be deployed on any machine that has Docker installed.

### What is "Jorkie Server"

The Jorkie Server is the central component of the Jorkie system. The Jorkie Server is responsible for managing Jorkie Agents, scheduling reconnaissance scans, and storing the results of the scans. The Jorkie Server is a RESTful API that is used by the Jorkie Console to interact with the system.

## What is the MVP (Minimal Viable Product) of Jorkie?

The MVP of Jorkie is a system that allows users to deploy Jorkie Agents and view the results of reconnaissance scans. The MVP of Jorkie will consist of the following features:

Jorkie Server:

- Functional Database with API calls for interacting with the database
- Functional Notifications to at least one platform (Slack, Email, etc)
- Functional scheduled tasks for running Jorkie Agents

Jorkie Console:

- Ability to create "projects"
- Ability to add, change, and remove IP Addresses, dommain names, and ASN's from a projects scope.
- Ability to Enable/Disable Jorkie Agents for the specific project
- Ability to view the results of a reconnaissance scan
- Ability to enabled continious monitoring for a project through reoccurring scheduled tasks
- Ability to configure notifications to be notified on failure, discovery of new domains

Jorkie Agents:

- Ability to perform a single reconnaissance task
- Ability to report the results of the reconnaissance task to the Jorkie Server
- At least 5 Jorkie Agents that perform different reconnaissance tasks
- Ability to log the entirety of the command output and errors and communicate those logs to the Jorkie Server
- Ability to specify throttle limits for the Jorkie Agents
- Ability to connect to the Jorkie Agent via debug console where you are able to attach to the running process and see the output in real time

## What are the nice to haves?

Jorkie Server:

- TBA

Jorkie Console:

- TBA

Jorkie Agents:

- TBA

## When will the project be completed?

Once all functionality/features mentioned in the MVP have been implemented and are functional.
