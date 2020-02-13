# API documentation

------------


### First clone this repository
```shell
git clone https://github.com/soorajpazeekal/RESTAPI.git
```
> Highly recommended to use a virtual environment and activate it.


### Install requirements

```shell
pip  install -r requirements.txt
```

------------



### Make migrations
```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```


------------
### Sync database with models:
```shell
python manage.py migrate --run-syncdb
```

------------

### Run server:

```python
python manage.py runserver
```



## API Endpoint
#### Eg: http://localhost:8000/api/{endpoint}


------------



## API USEAGE:

##### Mainly two user privileges.
1. Staff User 
2. Regular User

### Register a staff user
> METHOD = POST
`http://localhost:8000/api/create-user/`
>content type = json
#### Example Request:
```json
{
	"username":"mytest",
	"password":"mytest",
	"staff":"True"
}
```
> For creating a STAFF account must include "staff" json key in your request


------------



### Register a normal user
```json
{
	"username":"mytest",
	"password":"mytest"
}
```
> No need to send staff key in your request.


------------



## Generating access token (JWT):
### API endpoint: 

**METHOD = POST**

`http://localhost:8000/api/token-auth/`

#### request body :
```json
{
	"username":"mytest",
	"password":"mytest"
}
```

------------



### Posting first  luggage accommodation facility post (STAFF USER):

**METHOD = POST**


`http://localhost:8000/api/edit-luggagepost/`
#### request body :


```json
{
	"created":"username",
	"Luggage_types":{
		"Wheeled Duffels":"1200",
		"Wheeled Luggage":"2000",
		"Carry-On Luggage":"1500",
		"Wheeled Backpacks":"2000",
		"Duffel Bags":"1300"
	},
	"max_items":"3",
	"status":"Open"  
}
```
###  **fields**
- "created" == username of the user,
- "Luggage_types" == list of luggage types and price.
- "max_items" == maximum number of allowed luggages
- "status" == accommodation is completed the maximum bookings
 

------------



### Retrieving the data:
**METHOD = GET**

`http://localhost:8000/api/edit-luggagepost/`


------------



### Updating booking status:
**METHOD = PUT**

> once booking is created, the current staff user does not able to create new bookings. 

**request body**

```json
{
	"created":"username",
	"Luggage_types":{
		"Wheeled Duffels":"1200",
		"Wheeled Luggage":"2000",
		"Carry-On Luggage":"1500",
		"Wheeled Backpacks":"2000",
		"Duffel Bags":"1300"
	},
	"max_items":"3",
	"status":"Open"
}
```
> #### OR
```json
{
	"created":"username",
	"Luggage_types":{
		"Wheeled Duffels":"1200",
		"Wheeled Luggage":"2000",
		"Carry-On Luggage":"1500",
		"Wheeled Backpacks":"2000",
		"Duffel Bags":"1300"
	},
	"max_items":"3",
	"status":"Close"  <-- changes
}
```



------------


### Booking (Normal User) 
**METHOD = POST**
##### endpoint:
`http://localhost:8000/api/order/`

> request body:

```json
{
	"Luggage_types":{
		"Wheeled Duffels":"1200",
		"Wheeled Luggage":"2000"
	}
}
```

------------




### Retrieving the  luggage accommodation facilitys:
**METHOD = GET**

#### endpoint

`http://localhost:8000/api/order/`

### Retrieving users bookings as (STAFF USER)

**METHOD = GET**

**endpoint**

`https://localhost:8000/api/orders/`


------------




## EVERY ENDPOINT MUST NEED A JWT TOKEN.  
