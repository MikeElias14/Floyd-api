# TODO: Tempalte the xxxx_to_json's in terms of the model, not like this


def user_to_json(user):
    result = None
    if user is not None:
        result = dict(
            id=user.id,
            name=user.name
        )
    return result


def holding_to_json(holding):
    result = None
    if holding is not None:
        result = dict(
            id=holding.id,
            ticker=holding.ticker,
            name=holding.name
        )
    return result


def user_holdings_to_json(user_holdings):
    result = dict()
    if user_holdings is not None:
        for holding in user_holdings:
            result[holding.id] = dict(
                holding_id=holding.holding_id,
                user_id=holding.user_id,
                amount=holding.amount,
                ticker=holding.ticker,
                name=holding.name
            )
    return result
