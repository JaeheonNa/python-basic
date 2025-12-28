from fastapi import APIRouter, Depends

from database.repository import UserRepository
from schema.request import SignUpRequest
from schema.response import UserSchema
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