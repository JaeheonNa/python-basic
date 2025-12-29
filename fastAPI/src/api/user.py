<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException

from database.repository import UserRepository
from schema.request import SignUpRequest, SignInRequest
from schema.response import UserSchema, JWTResponse
from service.user import UserService
from database.orm import User
=======
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks

from database.repository import UserRepository
from schema.request import SignUpRequest, SignInRequest, CreateOTPRequest, VerifyOTPRequest
from schema.response import UserSchema, JWTResponse
from security import get_access_token
from service.user import UserService
from database.orm import User
from cache import redis_client
>>>>>>> macbook-pro-m3

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
<<<<<<< HEAD
        raise HTTPException(status_code=404, detail="User not found")
=======
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/email/otp")
def create_otp_handler(
        request: CreateOTPRequest,
        _: str = Depends(get_access_token),
        user_service: UserService = Depends(UserService)
):
    otp: int = user_service.create_otp()
    redis_client.set(request.email, otp)
    redis_client.expire(request.email, 3 * 60) # 3분

    # Todo : send email
    return {"otp": otp}

@router.post("/email/otp/verify")
def verify_otp_handler(
        request: VerifyOTPRequest,
        backgroundTasks: BackgroundTasks,
        access_token: str = Depends(get_access_token),
        user_service: UserService = Depends(UserService),
        user_repo: UserRepository = Depends(UserRepository)
):
    otp: str | None = redis_client.get(request.email)
    print("otp: ", int(otp))
    print("request.otp: ", request.otp)
    if otp is None or int(otp) != request.otp:
        raise HTTPException(status_code=400, detail="Bad Request")

    username = user_service.decode_jwt(access_token=access_token)
    user: User | None = user_repo.get_user_by_username(username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Todo save user email
    # user.email = request.email
    # user: User = user_repo.create_user(user)

    # backgroundTasks: 별도 스레드로 동작함.
    backgroundTasks.add_task(
        user_service.send_email_to_user,
        email=request.email
    )
    return UserSchema.model_validate(user)
>>>>>>> macbook-pro-m3
