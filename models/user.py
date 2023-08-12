#!/usr/bin/python3

from models.base_model import BaseModel

"""discription"""


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
