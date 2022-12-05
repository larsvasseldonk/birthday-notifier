# birthday-notifier

## Azure Resources

### Resources

The following resources need to be created:

- A resourcegroup (`rg-bdn-dev`) to cluster all related resources for the project.
- A storage account (`sabdndev`) to store data.

### Naming conventions

In Azure, we use the following naming conventions:

- `bdn`: birthday-notifier
- `rg`: resourcegroup
- `fa`: function app
- `asp`: app service plan
- `sa`: storage account
- `cs`: communication service
- `ecsd`: email communication services domain
- `ecs`: email communcation service
- `ap`: application insights
- `log`: log analytics space

Each development resource is called: `<resource_abbre>-bdn-dev`. 

## Running the app

Run, from the root folder: `python3 src/main.py`

# To test the function app locally

Install [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Clinux%2Ccsharp%2Cportal%2Cbash) on your system.

Activate your local environment: `. venv/bin/activate`

Run `func start` Core Tools command in your command line to start the app.

When the project is running, you can use the `Execute Function Now...` feature of the extension to trigger your functions as you would when the project is deployed to Azure. With the project running in debug mode, breakpoints are hit in Visual Studio Code as you would expect.