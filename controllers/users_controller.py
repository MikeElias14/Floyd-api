from models.model import Users, UserHoldings, Holdings
from controllers.convert_json import user_to_json


# Get user by name, everything else will work off of user ID
def get_user_by_name(name):
    query = Users.query.filter(Users.name == name).first()
    result = user_to_json(query)
    return result


def get_user_holdings(user_id):
    print()