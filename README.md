# Azure OpenAI Keyless Deployment

The purpose of this repository is to provision an Azure OpenAI account with an RBAC role permission for your user account to access,
so that you can use the OpenAI API SDKs with keyless (Entra) authentication. By default, the account will include a gpt-3.5 model, but you can modify `infra/main.bicep` to deploy other models instead.

## Prerequisites

1. Sign up for a [free Azure account](https://azure.microsoft.com/free/) and create an Azure Subscription.
2. Request access to Azure OpenAI Service by completing the form at [https://aka.ms/oai/access](https://aka.ms/oai/access) and awaiting approval.
3. Install the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). (If you open this repository in Codespaces or with the VS Code Dev Containers extension, that part will be done for you.)

## Provisioning

1. Login to Azure:

    ```shell
    azd auth login
    ```

2. Provision the OpenAI account:

    ```shell
    azd provision
    ```

    It will prompt you to provide an `azd` environment name (like "chat-app"), select a subscription from your Azure account, and select a [location where the OpenAI model is available](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) (like "francecentral"). Then it will provision the resources in your account and deploy the latest code. If you get an error or timeout with deployment, changing the location can help, as there may be availability constraints for the OpenAI resource.

3. When `azd` has finished, you should have an OpenAI account you can use locally when logged into your Azure account. You can output the necessary environment variables into an `.env` file like so:

    ```shell
    azd env get-values > .env
    ```

4. Then you can run the example code in this repository.


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


## Creating a new azd enviroment 

1. If you'd like to create a new Python project, you can create a new azd environment for it.

Create a new environment and set it as the default by running:

    ```shell
    azd env new <environment>
    ```

2. You can view the new environment and any previous environments you created by looking in the `.azure`folder, or by running the command: 

    ```shell
    azd env list
    ```

3. To change back to the previous azd environment:

    ```shell
    azd env select <environment> 
    ```