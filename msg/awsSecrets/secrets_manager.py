

class SecretsManager:
    def __init__(self):
        self.username = 'sample_username'
        self.password = 'sample_password'
        self.hostname = 'sample_hostname'

    def get_secret_values(self):
        secret_values = {self.username, self.password, self.hostname}
        return secret_values