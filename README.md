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
In the video module, we have 1 APIs

```python
>>> ks.VideoClassify()
``` 
---
### `k_sequencing.texts` module
In the text module, we have 3 APIs

```python
>>> ks.CategoryClassify()
>>> ks.Conversation()
>>> ks.ClosedQuestion()
``` 
---
### `k_sequencing.predictions` module
In the prediction module, we have 1 APIs

```python
>>> ks.Predictor()
``` 

# Demo and Usage
 - Image Documentation [link]
 - Video Documentation [link]
 - Text Documentation [link]
 - AI/Prediction Documentation [link]


## Working with response
### `k_sequencing.responses` module
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

To get meta data such as pagination

```python 
>>> result.meta # {'code': 200, 'message': 'success'}
```
