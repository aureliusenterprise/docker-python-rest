# docker-python-rest

This is a set of APIs for different services.
- '/data2model'
- '/consistency_metrics'
- '/compare'
- '/lineage_model'
- '/data_governance'


## Building / Running in docker
Create a new version of the container
```
make build
```

Run the container
```
make run
```

Stop the container
```
make kill
```

Run container with development vars
```
docker run --detach -p 5000:5000 rest-services
```

access service at ``http://localhost:5000/{service_name}``

Check if the service is running at ``http://localhost:5000/{service_name}/heartbeat``

# build and push docker container
docker build -t wombach/docker-python-rest:1.0.5 .
docker push wombach/docker-python-rest:1.0.5 

deployed REST APIs
 - '/data2model': data2model,
 - '/consistency_metrics': consistency_metrics,
 - '/compare': compare,
 -  '/lineage_model': lineage_model,
 -  '/data_governance': data_governance_dashboard,
 -  '/logging': elastic_logging,
 -  '/lineage_rest_api': register_get_app()

relevant links:
 - http://localhost:5000/lineage/heartbeat
 - http://localhost:5000/lineage/lin_api/