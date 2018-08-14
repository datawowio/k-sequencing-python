
# k-sequencing-python
k-sequencing-python is rest library for python version. 
###### support or question support@datawow.io

# Installation 
```
pip install k-sequencing
```
or
```
pip2 install k-sequencing
```

Python supports the following Python versions:

* Python 2.7 tested
* Python 3.5 tested
* Python 3.6 tested  

**Recommendation:**  We've created virtual-env for Python 3.5 on development process, thus recommended to use Python version 3.5 or later. 

For user who use **conda**, we haven't contribute yet


# Usage


## Import 
```python
>>> import k_sequencing as ks
```
 There are 4 modules for API that you can specific the module as your expected 
 
1. Image API module
```python
>>> import k_sequencing.images as ks
``` 
2. Text API module
```python
>>> import k_sequencing.texts as ks
``` 

3. Video API module
```python
>>> import k_sequencing.videos as ks
``` 

4. AI/Prediction API module
```python
>>> import k_sequencing.predictions as ks
``` 


## Functions explanation 
### `k_sequencing.images` module
In the image module, we have 4 APIs

```python
>>> ks.Choice()
>>> ks.Message()
>>> ks.PhotoTag()
>>> ks.ClosedQuestion()
``` 
---
### `k_sequencing.videos` module
In the image module, we have 1 APIs

```python
>>> ks.VideoClassify()
``` 
---
### `k_sequencing.texts` module
In the image module, we have 3 APIs

```python
>>> ks.CategoryClassify()
>>> ks.Conversation()
>>> ks.ClosedQuestion()
``` 
---
### `k_sequencing.predictions` module
In the image module, we have 1 APIs

```python
>>> ks.Predictor()
``` 


## Example

### `k_sequencing.images` modules

#### Choice class
Description: Yes or No Question from Image

### Create
```python
>>> """ To import 
>>> from k_sequencing.images import Choice as choice
>>>  or
>>> import k_sequencing.images as image
>>> """
>>> """ To use function
>>> result = image.Choice('PROJECT KEY').create(params=param)
>>> or
>>> result = choice('PROJECT KEY').create(params=param)
>>> """
```
#### params 

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   **Yes** | Tell moderator what answer you expected and what image is|
|categories | Array[string]     |    **Yes** | List of answers that you were expected. sparate by use space |
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      |  No | URL for answer callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| allow_empty	     | boolean      |   No |Allow answer can be blank. default is `false`|
|multiple | boolean   |    No | Configuration for multiple selection of category to answer default is `false` |
| custom_id	     | string      |   No |Custom ID that used for search|

#### response 
```python
print(result.data)

"""
{
   'allow_empty': False,
   'answer': [],
   'categories': ['face'],
   'credit_charged': 0,
   'custom_id': None,
   'data': 'image URL',
   'id': '5b72533e5a5e43c6b3909b9f',
   'instruction': 'face',
   'multiple': False,
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 139,
   'status': 'unprocess'
 }
 """
```

### Retrieve list of Image choices

You can retrieve data by use same object of connector that you have been created with you project key

```python
>>> """ let say your were imported """
>>> """ from k_sequencing.images import Choice as choice """
>>> result = choice('PROJECT KEY').list()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

##### response
```python
 print(result.data)
 
 """
 {
   'images': [{'allow_empty': False,
   'answer': [],
   'categories': ['face'],
   'credit_charged': 0,
   'custom_id': None,
   'data': 'image URL',
   'id': '5b72533e5a5e43c6b3909b9f',
   'instruction': 'face',
   'multiple': False,
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 139,
   'status': 'unprocess'},
   {...}, 
   {...}
  ]}
 """
```

### Retrieve data by ID of image

```python
>>> """ let say your were imported"""
>>> """ from k_sequencing.images import Choice as choice """
>>> result = choice("PROJECT KEY").find_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|

##### response
```python
 print(result.data)
 
"""
{
   'allow_empty': False,
   'answer': [],
   'categories': ['face'],
   'credit_charged': 0,
   'custom_id': None,
   'data': 'image URL',
   'id': '5b72533e5a5e43c6b3909b9f',
   'instruction': 'face',
   'multiple': False,
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 139,
   'status': 'unprocess'
}
 """
```

## Closed questions
[Standard Criteria]

### Create
```python
>>> """ To import 
>>> from k_sequencing.images import ClosedQuestion as closed
>>>  or
>>> import k_sequencing.images as image
>>> """
>>> """ To use function
>>> result = image.Choice('PROJECT KEY').create(params=param)
>>> or
>>> result = closed('PROJECT KEY').create(params=param)
>>> """
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      | No | URL for answer callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|

#### response
```python
 print(result.data)
 
"""
{
  'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'image URL',
  'id': '5b72604f5a5e43c6b2909b9f',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 140,
  'staff_id': None,
  'status': 'unprocess'
 }
 """
```

### Retrieve list of data

You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> """ let say your were imported """
>>> """ from k_sequencing.images import ClosedQuestion as closed """
>>> result = closed('PROJECT KEY').list()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

```python
print(result.data)

"""
{
   'answer': None,
   'credit_charged': 0,
   'custom_id': None,
   'data': 'image URL',
   'id': '5b72604f5a5e43c6b2909b9f',
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 140,
   'staff_id': None,
   'status': 'unprocess'}, 
   {...}, 
   {...}]
}
 """
```

### Retrieve data by ID of image

```python
>>> """ let say your were imported"""
>>> """ from k_sequencing.images import ClosedQuestion as closed """
>>> result = closed("PROJECT KEY").find_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
| custom_id | string     |    No | Client's image id |

##### response
```python
print(result.data)

{
  'image': {'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'image URL',
  'id': '5b72604f5a5e43c6b2909b9f',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 140,
  'staff_id': None,
  'status': 'unprocess'}
}
```



## Image messages
[Message Question from Image]

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> ks = k_sequencing
>>> result = ks.Message("PROJECT KEY").create(params=param)
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
>>> ks = k_sequencing
>>> result = ks.Message("PROJECT KEY").list()
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
>>> ks = k_sequencing
>>> result = ks.Message("PROJECT KEY").find_id("YOUR IMAGE ID")
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
>>> ks = k_sequencing
>>> result = ks.PhotoTag("PROJECT KEY").create(params=param)
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
>>> ks = k_sequencing
>>> result = ks.PhotoTag("PROJECT KEY").list()
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
>>> ks = k_sequencing
>>> result = ks.PhotoTag("PROJECT KEY").find_id("YOUR IMAGE ID")
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

- Standard Criteria
- Nudity/Sexual
- Demographic
- Standard Criteria & Human

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> ks = k_sequencing
>>> result = ks.Prediction("PROJECT KEY").create(params=param)
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
>>> ks = k_sequencing
>>> result = ks.Prediction("PROJECT KEY").list()
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
>>> ks = k_sequencing
>>> result = ks.Prediction("PROJECT KEY").find_id("YOUR IMAGE ID")
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
#### Standard Criteria

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
#### Nudity/Sexual
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
#### Demographic
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
#### Standard Criteria & Human
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
