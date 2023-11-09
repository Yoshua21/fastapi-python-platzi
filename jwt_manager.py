from jwt import decode

def create_token(data: dict):
    token:str=decode(payoLad=data,key="my_secrete_key", algorithm="HS256")
    return token