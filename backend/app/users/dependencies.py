from fastapi import Request, HTTPException, status, Depends, Cookie
from jose import jwt, JWTError
from datetime import datetime, timezone
from app.config import get_auth_data
from app.exceptions import TokenExpiredException, NoJwtException, NoUserIdException, ForbiddenException, TokenNoFound, TokenInvalidException
from app.users.dao import UsersDAO
from app.users.models import User


def get_token(users_access_token: str = Cookie(None)):
    if not users_access_token:
        raise TokenNoFound
    return users_access_token


async def get_current_user(token: str = Depends(get_token)):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=[auth_data['algorithm']])
        user_id: str = payload.get('sub')
        if user_id is None:
            raise TokenInvalidException
    except JWTError:
        raise TokenInvalidException
    
    user = await UsersDAO.find_one_or_none_by_id(int(user_id))
    if user is None:
        raise TokenInvalidException
    return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.is_admin:
        return current_user
    raise ForbiddenException
