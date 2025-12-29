from database.repository import UserRepository
from service.user import UserService
from database.orm import User


def test_user_sign_up(test_client, mocker):
    hash_password = mocker.patch.object(
        UserService,
        "hash_password",
        return_value="hashed"
    )

    user_create = mocker.patch.object(
        User,
        "create",
        return_value=User(id=None, username="test", password="hashed")
    )

    mocker.patch.object(
        UserRepository,
        "create_user",
        return_value=User(id=1, username="test", password="hashed")
    )

    body = {
        "username": "test",
        "password": "plain"
    }

    response = test_client.post("/users/sign-up", json=body)
    hash_password.assert_called_once_with(plain_password="plain")
    user_create.assert_called_once_with(username="test", hashed_password="hashed")
    assert response.status_code == 201
<<<<<<< HEAD
    assert response.json() == {"id":1, "username":"test"}
=======
    assert response.json() == {"id":1, "username":"test"}

def test_user_log_in(test_client, mocker):
    # 200
    user = mocker.patch.object(
        UserRepository, "get_user_by_username",
        return_value=User(id=1, username="admin", password="hashed")
    )
    verified = mocker.patch.object(
        UserService,
        "verify_password",
        return_value=True
    )
    access_token= mocker.patch.object(
        UserService,
        "create_jwt",
        return_value="access_token"
    )

    body = {
        "username": "admin",
        "password": "password"
    }
    response = test_client.post("/users/log-in", json=body)
    user.assert_called_once_with(username=body["username"])
    verified.assert_called_once_with(plain_password="password", hashed_password="hashed")
    access_token.assert_called_once_with(username="admin")
    assert response.status_code == 200
    assert response.json() == {"access_token":"access_token"}

    #401
    verified = mocker.patch.object(
        UserService,
        "verify_password",
        return_value=False
    )
    body = {
        "username": "admin",
        "password": "None"
    }
    response = test_client.post("/users/log-in", json=body)
    assert response.status_code == 401
    assert response.json() == {"detail": "Not Authorized"}

    #404
    mocker.patch.object(
        UserRepository, "get_user_by_username",
        return_value=None
    )
    body = {
        "username": "None",
        "password": "password"
    }
    response = test_client.post("/users/log-in", json=body)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
>>>>>>> macbook-pro-m3
