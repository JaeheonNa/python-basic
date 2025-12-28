import bcrypt
from jose import jwt
from datetime import datetime, timedelta

class UserService:

    encoding: str = "UTF-8"
    secret_key: str = "334b2b8a8201079679994c644733c2f959c0991b45d6be50f2644eab0c84f2f8"
    jwt_algorithm: str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            bcrypt.gensalt()
        )
        return hashed_password.decode(self.encoding)

    def verify_password(
            self,
            plain_password: str,
            hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )

    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub": username, # unique id
                "exp": datetime.now() + timedelta(days=1)
            },
            self.secret_key,
            algorithm=self.jwt_algorithm
        )