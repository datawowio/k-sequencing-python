### `k_sequencing.images` modules

## Choice class
Description: Yes or No Question from Image

### Create
```python
>>> from k_sequencing.images import Choice as choice
>>> result = choice('PROJECT KEY').create(params=param)
```
#### params 

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction| string|**Yes**| Tell moderator what answer you expected and what image is|
|categories | Array[string]|**Yes** | List of answers that you were expected. sparate by use space |
| data |string | **Yes** |URL of image|
| postback_url| string|No| URL for answer callback once image has been checked|
| postback_method|string | No |Configuration HTTP method GET POST PUT PATCH|
| allow_empty| boolean|No|Allow answer can be blank. default is `false`|
|multiple | boolean | No | Configuration for multiple selection of category to answer default is `false` |
| custom_id | string | No |Custom ID that used for search|

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

## Closed Question class
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
#### params
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
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|

#### response
```python
print(result.data)

"""
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
"""
```


## Image messages
Description: Message Question from Image

### Create
```python
>>> from k_sequencing.images import Message as message
>>> result = message("PROJECT KEY").create(params=param)
```

#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   **Yes** | Tell moderator what answer you expected and what image is|
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      | No | URL for callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|

#### response 
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
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|

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
Description: Tag an object in the image

### Create
```python
>>> from k_sequencing.images import PhotoTag as photo_tag
>>> result = photo_tag("PROJECT KEY").create(params=param)
```

#### params
| Field | Type| Required | Description |
| ------------- |:-------------:| :-----:| :-----|
|instruction| string|**Yes** |Tell moderator what answer you expected and what image is|
|data|string| **Yes** |URL of image|
|postback_url|string| No |URL for callback once image has been checked|
|postback_method|string | No |Configuration HTTP method GET POST PUT PATCH|
|custom_id|string|No|Custom ID that used for search|

#### response 
```python
print(result.data)

"""
{
 'answer': [],
 'credit_charged': 0,
 'custom_id': None,
 'data': 'Image URL',
 'id': '5b7296465a5e4318c1f990f4',
 'instruction': 'face',
 'postback_url': 'http://localhost:3000/callbacks',
 'processed_at': None,
 'project_id': 142,
 'status': 'unprocess'
}
"""
```

### Retrieve list of photo tag

```python 
>>> from k_sequencing.images import PhotoTag as photo_tag
>>> result = photo_tag("PROJECT KEY").list()
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |

#### response 
```python
print(result.data)

"""
{
   'images': [{'answer': [],
   'credit_charged': 0,
   'custom_id': None,
   'data': 'Image URL',
   'id': '5b7296465a5e4318c1f990f4',
   'instruction': 'face',
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 142,
   'status': 'unprocess'},
   {...}, 
   {...}]
}
"""
```

### Retrieve data by ID of image
```python
>>> from k_sequencing.images import PhotoTag as photo_tag
>>> result = photo_tag("PROJECT KEY").find_id("YOUR IMAGE ID")
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|

#### response 
```python
print(result.data) 

"""
{
  'image': {'answer': [],
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Image URL',
  'id': '5b7296465a5e4318c1f990f4',
  'instruction': 'face',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 142,
  'status': 'unprocess'}
}
"""
```
