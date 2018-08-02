def path(type_url, model):
    url = {
        "images": {
            "closed_questions": "images/closed_questions",
            "messages": "images/messages",
            "choices": "images/choices",
            "photo_tag": "images/photo_tags",
            "find": "projects/images/"},
        "videos": {"closed_questions": "videos/closed_questions"},
        "texts": {"categories": "v1/text/text_categories"},
        "ai": {
            "predictor": "prime/predictions",
            "find": "projects/images/"}
    }

    return url[type_url][model]


def base_url(model):
    url = {"images": "http://localhost:3001/api/", "videos": "http://localhost:3001/api/",
           "texts": "http://localhost:3002/api/", "ai": "http://localhost:3001/api/"}
    return url[model]
