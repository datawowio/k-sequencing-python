### `k_sequencing.images` modules

#### Choice class
Description: Yes or No Question from Image

### Create
```python
>>> from k_sequencing.images import Choice as choice
>>> result = choice('PROJECT KEY').create(params=param)
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

```python
>>> from k_sequencing.images import Choice as choice
>>> result = choice('PROJECT KEY').list()
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	integer | No | default 0|
| per_page 	     | string      | No | default 20 |

#### response
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
>>> from k_sequencing.images import Choice as choice
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

#### Closed Question class
Description: Standard Criteria

### Create
```python
>>> from k_sequencing.images import ClosedQuestion as closed
>>> result = closed('PROJECT KEY').create(params=param)
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

```python 
>>> from k_sequencing.images import ClosedQuestion as closed
>>> result = closed('PROJECT KEY').list()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	integer | No | default 0|
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
>>> from k_sequencing.images import ClosedQuestion as closed
>>> result = closed("PROJECT KEY").find_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|

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
Description: Message Question from Image

### Create
```python
>>> from k_sequencing.images import Message as message
>>> result = message("PROJECT KEY").create(params=param)
```

##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   **Yes** | Tell moderator what answer you expected and what image is|
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      | No | URL for callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|

##### response 
```python 
print(result.date)

"""
{
  'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Image URL',
  'id': '5b7270c25a5e431052f990f4',
  'instruction': 'face',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 141,
  'status': 'unprocess'
}
"""
```

### Retrieve list of Image messages

```python 
>>> from k_sequencing.images import Message as message
>>> result = message("PROJECT KEY").list()
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	integer | No | default 0|
| per_page 	     | string      | No | default 20 |

##### response 
```python
print(result.data)

"""
{
  'images': [{'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Image URL',
  'id': '5b7270c25a5e431052f990f4',
  'instruction': 'face',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 141,
  'status': 'unprocess'},
  {...}, 
  {...}]
}
"""

```

### Retrieve data by ID of image

```python
>>> from k_sequencing.images import Message as message
>>> result = message("PROJECT KEY").find_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| id	     | string      |   No | Image id|
|custom_id | string     |    No | Client's image id |

##### response 
```python
print(result.data)

"""
{
  'image': {'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Image URL',
  'id': '5b7270c25a5e431052f990f4',
  'instruction': 'face',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 141,
  'status': 'unprocess'}
}
"""
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
