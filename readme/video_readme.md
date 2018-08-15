###  `k_sequencing.videos` modules

# Table of Content
- [Video classify class](#video-classify-class)

## Video classify class
Description: Video classification

### Create
```python
>>> from k_sequencing.videos import VideoClassify as video
>>> result = video('PROJECT KEY').create(params=param)
```

#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | **Yes** |URL of Video|
| play_at | float |No |Setting video start time|
| allow_seeking |bool| No |Allow seeking video player (default `true`)|
|muted |bool|No| Mute video on start (default: `true`)|
| postback_url	     | string      | No | URL for answer callback once video has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|

#### response
```python
 print(result.data)
 
"""
{
  'allow_seeking': True,
  'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Video URL',
  'id': '5b72ad495a5e43286f5a0af3',
  'muted': True,
  'play_at': 0.0,
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 144,
  'status': 'unprocess'
}
 """
```

### Retrieve list of data

```python 
>>> from k_sequencing.videos import VideoClassify as video
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
   'videos': [{'allow_seeking': True,
   'answer': None,
   'credit_charged': 0,
   'custom_id': None,
   'data': 'Video URL',
   'id': '5b72ad495a5e43286f5a0af3',
   'muted': True,
   'play_at': 0.0,
   'postback_url': 'http://localhost:3000/callbacks',
   'processed_at': None,
   'project_id': 144,
   'status': 'unprocess'},
   {...},
   {...}]
}
 """
```

### Retrieve data by ID of video

```python
>>> from k_sequencing.videos import VideoClassify as video
>>> result = closed("PROJECT KEY").find_id("YOUR VIDEO ID")
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| video_id	     | string  |   **Yes** | Video's ID or custom ID which is you were assigned|

#### response
```python
print(result.data)

"""
{
  'video': {'allow_seeking': True,
  'answer': None,
  'credit_charged': 0,
  'custom_id': None,
  'data': 'Video URL',
  'id': '5b72ad495a5e43286f5a0af3',
  'muted': True,
  'play_at': 0.0,
  'postback_url': 'http://localhost:3000/callbacks',
  'processed_at': None,
  'project_id': 144,
  'status': 'unprocess'}
}
"""
```
