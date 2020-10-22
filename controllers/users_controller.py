from datetime import datetime
from extensions import db
from models.model import Users, UserHoldings, Holdings
from controllers.convert_json import user_to_json, user_holdings_to_json


# *** CREATE *** #

def create_user(name):
    if get_user_by_name(name) is not None:
        return 400, "This user already exists"

    cur_time = datetime.now()
    new_user = Users(
        name=name,
        created_at=cur_time,
        updated_at=cur_time
    )

    db.session.add(new_user)
    db.session.commit()

    return 200, ""


def add_user_holdings(user, holdings):
    user_holdings = get_user_holdings(user)
    for holding in holdings:  # Holdings of form [(ticker, amount)]


    db.session.add(new_user)
    db.session.commit()

    return 200, ""

# *** READ *** #

# Get user by name, everything else will work off of user ID
def get_user_by_name(name):
    query = Users.query.filter(Users.name == name).first()
    result = user_to_json(query)
    return result


def get_user_holdings(user_id):
    query = UserHoldings.query.filter(UserHoldings.user_id == user_id).all().join(Holdings)
    result = user_holdings_to_json(query)
    return result