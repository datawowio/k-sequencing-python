### `datawow.texts` modules

## Category class
Description: Classify type in many level of category type
```python
>>> from datawow.texts import CategoryClassify as cat
>>> result = cat('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| conversation| array of dict|**Yes**| Example: `[{ "name": "...", "message": "..." }]`|
|title|string|**Yes**|Title of conversation|
|allow_empty |bool| |No|Answer can be empty|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|


#### response 
```python
print(result.data)

"""
{
  'allow_empty': False,
   'categories': [],
   'conversation': [{'message': 'string', 'name': 'string'}],
   'created_at': '2018-08-15T10:11:17.493+07:00',
   'custom_id': 'string',
   'id': '5b7399d55a5e434994e3e0a4',
   'postback_method': 'string',
   'postback_url': 'string',
   'processed_at': None,
   'project_id': 145,
   'staff_id': None,
   'status': 'unprocessed',
   'title': 'string'
}
"""
```

## Retrieve list of text

```python
>>> from datawow.texts import CategoryClassify as cat
>>> result = cat('PROJECT KEY').list()
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
 [{'allow_empty': False,
  'categories': [],
  'conversation': [
      {'message': 'string', 'name': 'string'},
      {'message': 'string', 'name': 'string'}
  ],
  'created_at': '2018-08-15T11:14:01.029+07:00',
  'custom_id': None,
  'id': '5b73a8895a5e434994e3e0a9',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 145,
  'staff_id': None,
  'status': 'unprocessed',
  'title': 'test'}, 
  {...}, 
  {...}]
 """
```

### Retrieve data by ID of text

```python
>>> from datawow.texts import CategoryClassify as cat
>>> result = cat("PROJECT KEY").find_id("YOUR IMAGE ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| text_id	     | string  |   **Yes** | Text's ID or custom ID which is you were assigned|

#### response
```python
 print(result.data)
 
"""
{
  'allow_empty': False,
  'categories': [],
  'conversation': [
      {'message': 'string', 'name': 'string'},
      {'message': 'string', 'name': 'string'}
  ],
  'created_at': '2018-08-15T10:12:58.468+07:00',
  'custom_id': None,
  'id': '5b739a3a5a5e434994e3e0a6',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 145,
  'staff_id': None,
  'status': 'unprocessed',
  'title': 'test'
}
 """
```

## Closed Question class
Description: Classify inappropriate conversation
```python
>>> from datawow.texts import ClosedQuestion as close
>>> result = close('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
|data|string|**Yes**|Stream of text to moderate|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|


#### response 
```python
print(result.data)

"""
{
   'answer': '',
   'created_at': '2018-08-15T11:34:54.881+07:00',
   'custom_id': None,
   'data': 'test',
   'id': '5b73ad6e5a5e434994e3e0ab',
   'postback_method': 'GET',
   'postback_url': None,
   'processed_at': None,
   'project_id': 146,
   'staff_id': None,
   'status': 'unprocessed'
}
"""
```

## Retrieve list of text

```python
>>> from datawow.texts import ClosedQuestion as close
>>> result = close('PROJECT KEY').list()
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
 [{'answer': '',
  'created_at': '2018-08-15T11:34:54.881+07:00',
  'custom_id': None,
  'data': 'test',
  'id': '5b73ad6e5a5e434994e3e0ab',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 146,
  'staff_id': None,
  'status': 'unprocessed'},
  {...},
  {...}]
 """
```

### Retrieve data by ID of text

```python
>>> from datawow.texts import ClosedQuestion as close
>>> result = close("PROJECT KEY").find_id("YOUR TEXT ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| text_id	     | string  |   **Yes** | Text's ID or custom ID which is you were assigned|

#### response
```python
 print(result.data)
 
"""
{
  'answer': '',
  'created_at': '2018-08-15T11:34:54.881+07:00',
  'custom_id': None,
  'data': 'test',
  'id': '5b73ad6e5a5e434994e3e0ab',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 146,
  'staff_id': None,
  'status': 'unprocessed'
}
 """
```

## Conversation class
Description: Classify conversation
```python
>>> from datawow.texts import Conversation as conv
>>> result = conv('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
|conversation| array of dict|**Yes**| Example: `["foo", "bar"]`|
|custom_conversation_ids|string|**Yes**|Example: `['1','2']`|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|


#### response 
```python
print(result.data)

"""
{
  'answers': [''],
  'conversation': ['test', 'test'],
  'created_at': '2018-08-15T11:08:42.009+07:00',
  'custom_conversation_ids': ['1', '2'],
  'custom_id': None,
  'id': '5b73a74a5a5e434994e3e0a8',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 147,
  'staff_id': None,
  'status': 'unprocessed'
}
"""
```

## Retrieve list of text

```python
>>> from datawow.texts import Conversation as conv
>>> result = conv('PROJECT KEY').list()
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
 [{'answers': [''],
  'conversation': ['test', 'test'],
  'created_at': '2018-08-15T11:08:42.009+07:00',
  'custom_conversation_ids': ['1', '2'],
  'custom_id': None,
  'id': '5b73a74a5a5e434994e3e0a8',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 147,
  'staff_id': None,
  'status': 'unprocessed'},
  {...},
  {...}]
 """
```

### Retrieve data by ID of text

```python
>>> from datawow.texts import Conversation as conv
>>> result = conv("PROJECT KEY").find_id("YOUR TEXT ID")
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| text_id	     | string  |   **Yes** | Text's ID or custom ID which is you were assigned|

#### response
```python
 print(result.data)
 
"""
{
  'answers': [''],
  'conversation': ['test', 'test'],
  'created_at': '2018-08-15T11:08:42.009+07:00',
  'custom_conversation_ids': ['1', '2'],
  'custom_id': None,
  'id': '5b73a74a5a5e434994e3e0a8',
  'postback_method': 'GET',
  'postback_url': None,
  'processed_at': None,
  'project_id': 147,
  'staff_id': None,
  'status': 'unprocessed'
}
 """
```
