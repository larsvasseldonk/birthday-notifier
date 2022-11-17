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