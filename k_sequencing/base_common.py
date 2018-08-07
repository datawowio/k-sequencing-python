def path(type_url, model):
    url = {
        "images": {
            "closed_questions": "images/closed_questions",
            "messages": "images/messages",
            "choices": "images/choices",
            "photo_tag": "images/photo_tags",
            "find": "projects/images/"},
        "videos": {"closed_questions": "videos/closed_questions"},
        "texts": {"categories": "v1/text/text_categories", "conversations": "v1/text/text_closed_questions"},
        "ai": {
            "predictor": "prime/predictions",
            "find": "projects/images/"}
    }

    lv1 = url.get(type_url, {})
    final_path = lv1.get(model, "Not found")

    return final_path


def base_url(model):
    url = {"images": "http://localhost:3001/api/", "videos": "http://localhost:3001/api/",
           "texts": "http://localhost:3002/api/", "ai": "http://localhost:3001/api/"}

    return url.get(model, 'Not found')
