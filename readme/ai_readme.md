
### `k_sequencing.predictions` modules

Images (AI Beta)

- Standard Criteria
- Nudity/Sexual
- Demographic
- Standard Criteria & Human

### Create
```python
>>> from k_sequencing.predictions import Predictor as predict
>>> result = predict("PROJECT KEY").create(params=param)
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|

##### response 
```python

print(result.data)

"""
{
  'image': {'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Image URL',
  'id': '5b72a19c5a5e4318c0f990f3',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 143,
  'staff_id': None,
  'status': 'nanameue'}
}
"""
```

### Retrieve list of prediction
You can retrieve data by use same object of connector that you have been created with you project key

```python 
>>> from k_sequencing.predictions import Predictor as predict
>>> result = predict("PROJECT KEY").list()
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
   'images': [{'answer': None,
   'credit_charged': 0,
   'custom_id': None,
   'data': 'image URL',
   'id': '5b72a19c5a5e4318c0f990f3',
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 143,
   'staff_id': None,
   'status': 'nanameue'},
   {...}, 
   {...}]
}
"""
```

### Retrieve data by ID
all module of images is use same function to retrieve data with ID  
```python
>>> from k_sequencing.predictions import Predictor as predict
>>> result = predict("PROJECT KEY").find_id("YOUR IMAGE ID")
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| image_id | string  | **Yes** | Image's ID or custom ID which is you were assigned|

#### response 

```python
print(result.data)

"""
{
  'image': {'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'image URL',
  'id': '5b72a19c5a5e4318c0f990f3',
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 143,
  'staff_id': None,
  'status': 'nanameue'}
}
"""
```

### Response of each type AI
There are a difference type of response AI module here is a compare response of each
#### Standard Criteria
```python 
"""
{ 
  'image': { 'answer': 'approved',
  'credit_charged': 0,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a570d8860f4f17a353d313b',
  'postback_url': '[your callback URL]',
  'processed_at': None,
  'project_id': 87,
  'status': 'processing'}
}
"""
```
#### Nudity/Sexual
```python
"""
{ 
  'image': { 'answer': { 'sexual': 0.0003511860850267112 } ,
  'credit_charged': 1,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a547c1660f4f17a353d310c',
  'postback_url': '[your URL]',
  'processed_at': '2018-01-11T11:53:15.197+07:00',
  'project_id': 81,
  'status': 'processed'}
}
"""
```
#### Demographic
```python
"""
{ 
  'data': { 'answer': { 'result': [ 
   { 'age': 25,
     'age_prob': 0.08679278939962387,
     'gender': 'male',
     'gender_prob': 0.9268079400062561,
     'positions': 
	    {  'h': 268.20000000000005,
           'w': 248.8,
           'x': 0,
           'y': 11.599999999999994
        }
     }
 ]},
  'credit_charged': 0,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a5706f460f4f17a353d313a',
  'postback_url': '[your callback URL]',
  'processed_at': '2018-01-11T13:40:57.789+07:00',
  'project_id': 80,
  'status': 'processed'}
}
"""
```
#### Standard Criteria & Human
```python
"""
{
  'data': { 'image': { 'answer': 'approved',
  'credit_charged': 1,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a547c1660f4f17a353d310c',
  'postback_url': '[your URL]',
  'processed_at': '2018-01-11T11:53:15.197+07:00',
  'project_id': 81,
  'status': 'processed'}}
}
"""
```
