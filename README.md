# k-sequencing-python
3rd for k-sequencing in python version 


# Installation 
```
pip install k-sequencing
```
or
```
pip2 install k-sequencing
```

Python supports the following Python versions:

* Python 2.7


# Usage


## Import 
```python
>>> import k_sequencing
```

## Choices
[Yes or No Question from Image (30 mins response time)]
### Create
```python
>>> param = {'instruction': 'face', 'categories': 'cat1 cat2 cat3', 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_choices(params=param)
```
##### params 
|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   Yes | Image instruction|
|categories | Array[string]     |    Yes | Categories of answers |
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      |  No | Image postback url|
|multiple | boolean   |    No | true for multiple answer and false for one answer |
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|
| allow_empty	     | boolean      |   No |Allow sent answer with empty choice. default is `false`|

### Retrieve list of Image choices

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_choices()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string  |   No | Image id|
|custom_id | string |    No | Client's image id |


## Closed questions
[Standard Criteria (5 mins response time)]

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_closed_questions(params=param)
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | Yes |Data for moderate|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|
### Retrieve list of data

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_closed_questions()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |
### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
| custom_id | string     |    No | Client's image id |

## Image messages
[Message Question from Image (30 mins response time)]

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_messages(params=param)
```

##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   Yes | Image instruction|
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|

### Retrieve list of Image messages

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_messages()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
|custom_id | string     |    No | Client's image id |

## Photo tags
[Tag an object in the image (60 mins response time)]

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_photo_tags(params=param)
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   Yes | Image instruction|
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|

### Retrieve list of photo tag

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_photo_tags()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

### Retrieve data by ID
all module of images is use same function to retrieve data with ID  
```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
|custom_id | string     |    No | Client's image id |






## Prediction
Images (AI Beta / 95% accuracy)

- [nanameue] Standard Criteria (~1 min)
- [sexual] Nudity/Sexual (~1 min)
- [demographic] Demographic (~3 mins)
- [ai_human] Standard Criteria & Human

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_preditcion(params=param)
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|

### Retrieve list of photo tag

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_prediction()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

### Retrieve data by ID
all module of images is use same function to retrieve data with ID  
```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
|custom_id | string     |    No | Client's image id |

There are a difference type of response AI module here is a compare response of each type
#### [nanameue] Standard Criteria (~1 min)
#### [sexual] Nudity/Sexual (~1 min)
#### [demographic] Demographic (~3 mins)
#### [ai_human] Standard Criteria & Human





# Response
To get response that data has been contained in response class you can call them by name for example
```python 
>>> result.data
```
Data it's Dict you can do as you want like a JSON object

For check error or status by calling this 

```python 
>>> result.error_code # 401
>>> result.message # Not authenticated
```

also you can get HTTP success by this

```python 
>>> result.success_code # 200
```
