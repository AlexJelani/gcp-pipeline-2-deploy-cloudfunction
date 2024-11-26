# Cloud Function Deployment

This repository contains a Google Cloud Function with automated deployment using Cloud Build.

## Project Structure

## Function Details
- Name: `function_1_v10`
- Runtime: Python 3.9
- Trigger: HTTP
- Region: us-central1
- Framework: Functions Framework 3.x

## Technical Implementation
The function accepts HTTP requests and processes them in the following way:
1. Checks for a 'name' parameter in the JSON body
2. If not found, checks query parameters
3. Falls back to default value 'V2.0'
4. Returns formatted response: "function {name}!"

## Development Setup

### Prerequisites
- Python 3.9 or higher
- Google Cloud SDK
- Access to a Google Cloud Project
- Git

### Local Environment Setup
1. Install Google Cloud SDK

brew install google-cloud-sdk
