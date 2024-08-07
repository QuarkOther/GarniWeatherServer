import os


class LoadEnvVars:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value


LoadEnvVars('conf/env.conf')

SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT = int(os.getenv('SERVER_PORT'))
