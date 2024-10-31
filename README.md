<!--
---
name: Azure OpenAI resource with keyless auth (Python)
description: Provision an Azure OpenAI resource with keyless authentication and use the Python OpenAI SDK to connect to it.
languages:
- python
- bicep
- azdeveloper
products:
- azure-openai
- azure
page_type: sample
urlFragment: azure-openai-keyless-python
---
-->
# Azure OpenAI resource with keyless auth (Python)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&skip_quickstart=true&machine=basicLinux32gb&repo=784926917&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=WestUs2)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Azure-Samples/azure-openai-keyless-python)

The purpose of this repository is to provision an Azure OpenAI account with an RBAC role permission for your user account to access,
so that you can use the OpenAI API SDKs with keyless (Entra) authentication.

* [Features](#features)
* [Getting started](#getting-started)
  * [GitHub Codespaces](#github-codespaces)
  * [VS Code Dev Containers](#vs-code-dev-containers)
  * [Local environment](#local-environment)
* [Deployment](#deployment)
* [Running the Python example](#running-the-python-example)
* [Guidance](#guidance)
  * [Costs](#costs)
  * [Security guidelines](#security-guidelines)
* [Resources](#resources)

## Features

* Provisions an Azure OpenAI account with keyless authentication enabled
* Grants the "Cognitive Services OpenAI User" RBAC role to your user account
* Deploys a gpt-4o-mini model by default, but you can modify the [Bicep template](infra/main.bicep) to deploy other models
* Example script uses the [openai](https://pypi.org/project/openai/) Python package to make a request to the Azure OpenAI API

### Architecture diagram

![Architecture diagram: Microsoft Entra managed identity connecting to Azure AI services](./diagram.png)

## Getting started

You have a few options for getting started with this template.
The quickest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also [set it up locally](#local-environment).

### GitHub Codespaces

You can run this template virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:

1. Open the template (this may take several minutes):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/azure-openai-keyless-python)

2. Open a terminal window
3. Continue with the [deployment steps](#deployment)

### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/azure-openai-keyless-python)

3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.
4. Continue with the [deployment steps](#deployment)

### Local environment

1. Make sure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.9+](https://www.python.org/downloads/)

2. Make a new directory called `azure-openai-keyless-python` and clone this template into it using the `azd` CLI:

    ```shell
    azd init -t azure-openai-keyless-python
    ```

    You can also use git to clone the repository if you prefer.

3. Continue with the [deployment steps](#deployment)

## Deployment

1. Login to Azure:

    ```shell
    azd auth login
    ```

    For GitHub Codespaces users, if the previous command fails, try:

   ```shell
    azd auth login --use-device-code
    ```

2. Provision the OpenAI account:

    ```shell
    azd provision
    ```

    It will prompt you to provide an `azd` environment name (like "chat-app"), select a subscription from your Azure account, and select a [location where the OpenAI model is available](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) (like "canadaeast"). Then it will provision the resources in your account and deploy the latest code.

    ⚠️ If you get an error or timeout with deployment, changing the location can help, as there may be availability constraints for the OpenAI resource. To change the location run:

    ```shell
    azd env set AZURE_LOCATION "yournewlocationname"
    ```

3. When `azd` has finished, you should have an OpenAI account you can use locally when logged into your Azure account. You can output the necessary environment variables into an `.env` file by running a script:

    For Mac OS X / Linux:

    ```shell
    ./write_dot_env.sh
    ```

    For Windows:

    ```shell
    pwsh ./write_dot_env.ps1
    ```

4. Then you can proceed to [run the Python example](#running-the-python-example).

## Running the Python example

1. If you're not already running in a Codespace or Dev Container, create a Python virtual environment.

2. Install the requirements:

    ```shell
    python -m pip install -r requirements.txt
    ```

3. Run the example:

    ```shell
    python example.py
    ```

    This will use the OpenAI API SDK to make a request to the OpenAI API and print the response.

## Guidance

### Costs

This template creates only the Azure OpenAI resource, which is free to provision. However, you will be charged for the usage of the Azure OpenAI chat completions API. The pricing is based on the number of tokens used, with around 1-3 tokens used per word. You can find the pricing details for the OpenAI API on the [Azure Cognitive Services pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).

### Security guidelines

This template uses [keyless authentication](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections) for authenticating to the Azure OpenAI resource. This is a secure way to authenticate to Azure resources without needing to store credentials in your code. Your Azure user account is assigned the "Cognitive Services OpenAI User" role, which allows you to access the OpenAI resource. You can find more information about the permissions of this role in the [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/role-based-access-control).

For further security, you could also deploy the Azure OpenAI inside a private virtual network (VNet) and use a private endpoint to access it. This would prevent the OpenAI resource from being accessed from the public internet.

## Resources

* [Video: Using keyless auth with Azure AI services](https://www.youtube.com/watch?v=IkDcQvKoQ8k)
* [Sample app: Azure OpenAI + Container Apps + Managed Identity](https://github.com/Azure-Samples/openai-chat-app-quickstart)
