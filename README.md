# k-sequencing-python
k-sequencing-python is rest library for python version.

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
[Yes or No Question from Image]
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

##### response 
```
{ 'code': 200,
  'data': { u'allow_empty': False,
            u'answer': [],
            u'categories': [u'face,', u'eye'],
            u'credit_charged': 0,
            u'custom_id': None,
            u'data': u'[image URL]',
            u'id': u'5a56c56f60f4f17a353d3113',
            u'instruction': u'face',
            u'multiple': False,
            u'postback_url': u'',[your url]
            u'processed_at': None,
            u'project_id': 82,
            u'status': u'unprocess'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

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

##### response
```
{ 'code': 200,
  'data': { u'image': { u'allow_empty': False,
                        u'answer': [],
                        u'categories': [u'face,', u'eye'],
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a56c56f60f4f17a353d3113',
                        u'instruction': u'face',
                        u'multiple': False,
                        u'postback_url': u'[your callback URL]',
                        u'processed_at': None,
                        u'project_id': 82,
                        u'status': u'unprocess'}},
  'error_code': None,
  'message': { u'code': 200,
               u'current_page': 1,
               u'message': u'success',
               u'next_page': -1,
               u'prev_page': -1,
               u'total_count': 2,
               u'total_pages': 1}}
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```
#### Note: your date is wrap into ```image``` 

### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string  |   No | Image id|
|custom_id | string |    No | Client's image id |

##### response
```
{ 'code': 200,
  'data': { u'images': [ { u'allow_empty': False,
                           u'answer': [],
                           u'categories': [u'face', u'ear'],
                           u'credit_charged': 0,
                           u'custom_id': None,
                           u'data': u'[image URL]',
                           u'id': u'5a546e4160f4f17a353d3106',
                           u'instruction': u'face',
                           u'multiple': False,
                           u'postback_url': u'[your callback URL]',
                           u'processed_at': None,
                           u'project_id': 82,
                           u'status': u'unprocess'} 
                           {...},
                           {...}]},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200,
            u'current_page': 1,
            u'message': u'success',
            u'next_page': -1,
            u'prev_page': -1,
            u'total_count': 3,
            u'total_pages': 1}}
```

## Closed questions
[Standard Criteria]

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

##### response
```
{ 'code': 200,
  'data': { u'answer': None,
            u'credit_charged': 0,
            u'custom_id': None,
            u'data': u'[image URL]',
            u'id': u'5a56d5ad60f4f17a353d3120',
            u'postback_url': u'your callback URL',
            u'processed_at': None,
            u'project_id': 86,
            u'status': u'unprocess'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

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

```
{ 'code': 200,
  'data': { u'images': [ { u'answer': None,
                           u'credit_charged': 0,
                           u'custom_id': None,
                           u'data': u'[image URL]',
                           u'postback_url': u'[your callback URL]',
                           u'processed_at': None,
                           u'project_id': 86,
                           u'status': u'unprocess'},
                           {...},
                           {...}]},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200,
            u'current_page': 1,
            u'message': u'success',
            u'next_page': -1,
            u'prev_page': -1,
            u'total_count': 3,
            u'total_pages': 1}}
```

### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
| custom_id | string     |    No | Client's image id |

##### response
```
{ 'code': 200,
  'data': { u'image': { u'answer': None,
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a56d5ad60f4f17a353d3120',
                        u'postback_url': u'[your callback URL]',
                        u'processed_at': None,
                        u'project_id': 86,
                        u'status': u'unprocess'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```



## Image messages
[Message Question from Image]

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

##### response 
```
{ 'code': 200,
  'data': { u'answer': None,
            u'credit_charged': 0,
            u'custom_id': None,
            u'data': u'[image URL]',
            u'id': u'5a56d8f660f4f17a353d3121',
            u'instruction': u'face',
            u'postback_url': u'[your callback URL]',
            u'processed_at': None,
            u'project_id': 84,
            u'status': u'unprocess'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

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

##### response 
```
{ 'code': 200,
  'data': { u'images': [ { u'answer': None,
                           u'credit_charged': 0,
                           u'custom_id': None,
                           u'data': u'[image URL]',
                           u'id': u'5a56d8f660f4f17a353d3121',
                           u'instruction': u'face',
                           u'postback_url': u'[your callback URL]',
                           u'processed_at': None,
                           u'project_id': 84,
                           u'status': u'unprocess'},
                           {...},
                           {...}]},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200,
            u'current_page': 1,
            u'message': u'success',
            u'next_page': -1,
            u'prev_page': -1,
            u'total_count': 3,
            u'total_pages': 1}}
```

### Retrieve data by ID of image

```python
>>> result = con.get_image_by_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
|custom_id | string     |    No | Client's image id |

##### response 
```
{ 'code': 200,
  'data': { u'image': { u'answer': None,
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a56d8f660f4f17a353d3121',
                        u'instruction': u'face',
                        u'postback_url': u'[your URL]',
                        u'processed_at': None,
                        u'project_id': 84,
                        u'status': u'unprocess'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```


## Photo tags
[Tag an object in the image]

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

##### response 
```
{ 'code': 200,
  'data': { u'answer': [],
            u'credit_charged': 0,
            u'custom_id': None,
            u'data': u'[image URL]',
            u'id': u'5a56da1460f4f17a353d3122',
            u'instruction': u'face',
            u'postback_url': u'[your callback URL]',
            u'processed_at': None,
            u'project_id': 85,
            u'status': u'unprocess'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

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

##### response 
```
{ 'code': 200,
  'data': { u'images': [ { u'answer': [],
                           u'credit_charged': 0,
                           u'custom_id': None,
                           u'data': u'[image URL]',
                           u'id': u'5a56da1460f4f17a353d3122',
                           u'instruction': u'face',
                           u'postback_url': u'[your image URL]',
                           u'processed_at': None,
                           u'project_id': 85,
                           u'status': u'unprocess'},
		            				   {...},
		            				   {...}]},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200,
            u'current_page': 1,
            u'message': u'success',
            u'next_page': -1,
            u'prev_page': -1,
            u'total_count': 3,
            u'total_pages': 1}}
```

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

##### response 
```
{ 'code': 200,
  'data': { u'image': { u'answer': [],
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a56da1460f4f17a353d3122',
                        u'instruction': u'face',
                        u'postback_url': u'',
                        u'processed_at': None,
                        u'project_id': 85,
                        u'status': u'unprocess'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

## Prediction
[Images (AI Beta)]

- [nanameue] Standard Criteria
- [sexual] Nudity/Sexual
- [demographic] Demographic
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

##### response 
```
{ 'code': 200,
  'data': { u'answer': None,
            u'credit_charged': 0,
            u'custom_id': None,
            u'data': u'[image URL]',
            u'id': u'5a57144660f4f17a353d313d',
            u'postback_url': u'[your callback URL]',
            u'processed_at': None,
            u'project_id': 87,
            u'status': u'processing'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

### Retrieve list of prediction
You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_prediction()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |


##### response 
```
{ 'code': 200,
  'data': { u'images': [ { u'answer': None,
                           u'credit_charged': 0,
                           u'custom_id': None,
                           u'data': u'[image URL]',
                           u'id': u'5a57144660f4f17a353d313d',
                           u'postback_url': u'[your callback URL]',
                           u'processed_at': None,
                           u'project_id': 87,
                           u'status': u'processing'},
                           {...},
		            				   {...}]},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200,
            u'current_page': 1,
            u'message': u'success',
            u'next_page': -1,
            u'prev_page': -1,
            u'total_count': 2,
            u'total_pages': 1}}
```

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


##### response 

```
{ 'code': 200,
  'data': { u'image': { u'answer': None,
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a57144660f4f17a353d313d',
                        u'postback_url': u'[your callback URL]',
                        u'processed_at': None,
                        u'project_id': 87,
                        u'status': u'processing'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```

### Response of each type AI
There are a difference type of response AI module here is a compare response of each
#### [nanameue] Standard Criteria

###### response 
```
{ 'code': 200,
  'data': { u'image': { u'answer': u'approved',
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a570d8860f4f17a353d313b',
                        u'postback_url': u'[your callback URL]',
                        u'processed_at': None,
                        u'project_id': 87,
                        u'status': u'processing'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```
#### [sexual] Nudity/Sexual
###### response 
```
{ 'code': 200,
  'data': { u'image': { u'answer': { u'sexual': 0.0003511860850267112 } ,
                        u'credit_charged': 1,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a547c1660f4f17a353d310c',
                        u'postback_url': u'[your URL]',
                        u'processed_at': u'2018-01-11T11:53:15.197+07:00',
                        u'project_id': 81,
                        u'status': u'processed'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```
#### [demographic] Demographic
###### response 
```
{ 'code': 200,
  'data': { u'answer': { u'result': [ 
						   { u'age': 25,
                             u'age_prob': 0.08679278939962387,
                             u'gender': u'male',
                             u'gender_prob': 0.9268079400062561,
                             u'positions': 
	                           { u'h': 268.20000000000005,
                                 u'w': 248.8,
                                 u'x': 0,
                                 u'y': 11.599999999999994
                               }
                            }
                          ]
                        },
                        u'credit_charged': 0,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a5706f460f4f17a353d313a',
                        u'postback_url': u'[your callback URL]',
                        u'processed_at': u'2018-01-11T13:40:57.789+07:00',
                        u'project_id': 80,
                        u'status': u'processed'},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```
#### [ai_human] Standard Criteria & Human
###### response 
```
{ 'code': 200,
  'data': { u'image': { u'answer': u'approved',
                        u'credit_charged': 1,
                        u'custom_id': None,
                        u'data': u'[image URL]',
                        u'id': u'5a547c1660f4f17a353d310c',
                        u'postback_url': u'[your URL]',
                        u'processed_at': u'2018-01-11T11:53:15.197+07:00',
                        u'project_id': 81,
                        u'status': u'processed'}},
  'error_code': None,
  'message': u'success',
  'meta': { u'code': 200, u'message': u'success'}}
```


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
>>> result.code # 200
```
