# training-project-lab
##### World maps is deployed and ready for consumption, check it here: [World maps](https://world-maps.nw.r.appspot.com/)

## World maps
A simple Python web application that displays various choropleth maps of the world 

You can run it on your machine, or deploy it yourself 

## Run it locally
#### Dependencies
Go to the project directory and execute the following command
```
pip install -r requirements.txt
```
 Or do things manually:

###### Using the package manager [pip](https://pip.pypa.io/en/stable/)

```
pip install dash
```
```
pip install plotly==4.12.0
```
```
pip install pandas
```
#### Run the application: ```python main.py```
## Deployment
1. Download and install [Cloud SDK](https://cloud.google.com/sdk/docs), or update: ```gcloud components update``` then launch it
2. Create a new project: ```gcloud projects create [YOUR_PROJECT_ID] --set-as-default```
3. Initialize GAE app and specify the project: ```gcloud app create --project=[YOUR_PROJECT_ID]```
4. Choose a [region](https://cloud.google.com/compute/docs/regions-zones)
5. Install the [gcloud component](https://cloud.google.com/sdk/docs/components) that includes extension for Pytohn 3: ```gcloud components install app-engine-python``` 
6. Deploy the application: ```gcloud app deploy```
7. Launch your browser to view the app: ```gcloud app browse```

For more information refer to google could [documentation](https://cloud.google.com/appengine/docs/standard/python3/building-app) for Python 3
