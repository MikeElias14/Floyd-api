# TODO: Tempalte the xxxx_to_json's in terms of the model, not like this


def user_to_json(user):

    result = dict(
        id=user.id,
        name=user.name
    )
    return result
