# k-sequencing-python
3rd for k-sequencing in python version 


# Installation 
```
pip install k_sequencing or pip2 install k_sequencing
```

Python supports the following Python versions:

* Python 2.7


# Usage


## Import 
```python
>>> import k_sequencing
```


## Image Choices

### Create
```python
>>> param = {'instruction': 'face', 'categories': 'cat1 cat2 cat3', 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_choices(params=param)
```

### Retrive list of Image choices

You can retrive data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_choices()
```

### Retrive data by ID of image

```python
>>> result = con.get_image_choices_id(params={"id": "YOUR IMAGE ID"})
```


## Image choices

### Create
```python
>>> param = {'instruction': 'face', 'categories': 'cat1 cat2 cat3', 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_choices(params=param)
```

### Retrive list of data

You can retrive data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_choices()
```

### Retrive data by ID of image

```python
>>> result = con.get_image_choices_id(params={"id": "YOUR IMAGE ID"})
```

## Image closed questions

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_closed_questions(params=param)
```

### Retrive list of data

You can retrive data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_closed_questions()
```

### Retrive data by ID of image

```python
>>> result = con.get_image_closed_questions_id(params={"id": "YOUR IMAGE ID"})
```

## Image message

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_messages(params=param)
```

### Retrive list of Image choices

You can retrive data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_messages()
```

### Retrive data by ID of image

```python
>>> result = con.get_image_messages_id(params={"id": "YOUR IMAGE ID"})
```

## Image Photo tags

### Create
```python
>>> param = {'instruction': 'face', 'data': 'URL_IMAGE'}
>>> con = k_sequencing.Connector('PROJECT_KEY')
>>> result = con.create_image_photo_tags(params=param)
```

### Retrive list of Image choices

You can retrive data by use same object of connector that you have been created with you project key

```python 
>>> result = con.get_image_photo_tags()
```

### Retrive data by ID of image

```python
>>> result = con.get_image_photo_tags_id(params={"id": "YOUR IMAGE ID"})
```

# Response
To get response that data has been containt in response class you can call them by 
```python 
>>> result.data
```
Data it's Dict you can do as you want like a json object other langauage 

to check error or status by calling this 

```python 
>>> result.error_code # 401
>>> result.message # Not authenticated
```

also you can get HTTP success by this

```python 
>>> result.success_code # 200
```
