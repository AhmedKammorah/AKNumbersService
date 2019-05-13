# AKNumberService 

Number Service

# The Problem Defention
The task is to write a tool that, given any number between 1 and 1,000 inclusive, returns the grammatically correct English phrase for this number (e.g. given 111 it shows “one hundred and eleven”, given 21 it shows “twenty-one”).
# The Solution


#### Simple Interface 
```
translate_number(number)

<!-- out put from API -->
{
  "number": 134,
  "number_en": "one hundred and thirty-four"
}
```
#### Service 



## Components 
1. Number util
2. Main Number Service 
4. Rest API Service 
6. some tests
7. API docs
8. Docker/Docker-compose and running scripts



# Getting Started

## steps 
* build docker image 
* Run docker compose 
	* Run Rest API Service 
* User Rest API
	* check api docs /apidocs
	* /api/auth to get token
	* /api/number/<number> [GET,POST] it is public for now
* Use RPC client


## Init
* clone this repo
* Code Dir Tree
	```
	./
		MainService/    <Your main  code dir> 
		Readme.md
		docker-entrypoint.sh
		..
	```

## Running Pre Requirements
#### Option 1 (Recommended)
	* Docker
	* Docker-compose
#### Option 2
	* Python 3.X
	* pip and python requirements in requirements.txt
		```
			pip install --no-cache-dir -r requirements.txt
		```

## Build

* Build The images
```
    cd $PWD
	sh build_docker_image.sh 

```
* OR Pull the image from Docker hub 
```
    cd $PWD
	docker pull ahmedkammorah/ak_numbers_service 

```
## Run
#### Start Container On (Dev Mode) 
```
	sh run_ak_dev.sh
```
##### Run test
```
python MainService/tests/test_ak_numbers_utils.py 
```

#### Start Container On (Pro Mode) 
```
	docker-compose up
```

## Use The Demo 
### Use Rest API
* Check The API Doc 
	* [Swagger API docs](http://localhost:5000/apidocs)
* Start Login to get the JWT Token to be able to user the send API Endpoint
	* [Auth Endpoint  /api/auth ](http://localhost:5000/apidocs/#/AKAuth)
		* username: <Main user name\>
		* password: <Main Password\>
* Test the token on the protected endpoint
	* [Protected test Endpoint /api/protected](http://localhost:5000/apidocs/#/AKAuth/get_api_protected)
* Use the send Numbers endpoint <not under AUTH for public use for now>
	* [Send Number Endpoint /api/number [GET, POST]](http://localhost:5000/apidocs/#/AKNumberServiceAPI/translateNumber)

# Author
* Ahmed Kammroah 
	* [ahmedkammorah](https://github.com/AhmedKammorah) 
	* [resume](https://github.com/AhmedKammorah/my_resume_latex)
	* [LinkedIn](https://www.linkedin.com/in/ahmedkammorah/)
