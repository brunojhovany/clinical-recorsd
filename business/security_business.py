import uuid
import hashlib


class PassworManager:
    def hashpassword(text_to_hash):
        salt = uuid.uuid4().hex
        return hashlib.sha512(salt.encode()+text_to_hash.encode()).hexdigest()+':'+salt

    def matchHashText(hashedText, providedText):
        _hashed_text, salt = hashedText.split(':')
        return hashedText == hashlib.sha512(salt.encode()+providedText.encode()).hexdigest()
