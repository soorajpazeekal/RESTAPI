# API documentation
### First clone this repository
`git clone https://github.com/soorajpazeekal/RESTAPI.git`
> Highly recommended to use a virtual environment and activate it.

### Make migrations
`python manage.py makemigrations`

`python manage.py migrate`

[========]

### Troubleshoot errors in migrations
> If facing some error like  'OperationalError No Such Table' while migrating:
`python manage.py migrate --run-syncdb`

## API Endpoint
#### Ex: http://localhost:8000/api/{endpoint}

[========]

## API USEAGE:

##### Mainly two user privileges.
1. Staff User 
2. Regular User

### Register a staff user
> METHOD = POST
`http://localhost:8000/api/create-user/`
>content type = json
#### Example Request:
`{
	"username":"mytest",
	"password":"mytest",
	"staff":"True"
}```
> For creating a STAFF account must include "staff" json key in your request

### Register a normal user
`{
	"username":"mytest",
	"password":"mytest"
}```
> No need to send staff key in your request.

## Generating access token (JWT):
### API endpoint: 
`http://localhost:8000/api/token-auth/`



