from fastapi import APIRouter, Depends, HTTPException

from database.repository import UserRepository
from schema.request import SignUpRequest, SignInRequest
from schema.response import UserSchema, JWTResponse
from service.user import UserService
from database.orm import User

# main에서 app에 추가해야함.
router = APIRouter(prefix="/users")

@router.post("/sign-up", status_code=201)
def user_sign_up_handler(
        request: SignUpRequest,
        user_service: UserService = Depends(UserService),
        user_repo: UserRepository = Depends(UserRepository)
 ):
    hashed_password = user_service.hash_password(plain_password=request.password)
    user: User = User.create(
        username=request.username,
        hashed_password=hashed_password
    )
    user: User = user_repo.create_user(user)
    return UserSchema.model_validate(user)

@router.post("/log-in", status_code=200)
def user_log_in_handler(
        request: SignInRequest,
        user_service: UserService = Depends(UserService),
        user_repo: UserRepository = Depends(UserRepository)
):
    user: User = user_repo.get_user_by_username(username=request.username)
    if user:
        verified: bool = user_service.verify_password(
            plain_password=request.password,
            hashed_password=user.password
        )
        if verified:
            access_token: str = user_service.create_jwt(username=user.username)
            return JWTResponse(access_token=access_token)
        else:
            raise HTTPException(status_code=401, detail="Not Authorized")
    else:
        raise HTTPException(status_code=404, detail="User not found")