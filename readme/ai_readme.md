### `k_sequencing.predictions` modules

Images (AI Beta)

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
