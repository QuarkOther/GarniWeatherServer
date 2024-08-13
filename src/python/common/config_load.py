import os


class LoadEnvVars:
    """
    A class to load environment variables from a file.

    Attributes:
    ----------
    file_path : str
        The path to the environment configuration file.
    """
    def __init__(self, file_path):
        """
        Constructs all the necessary attributes for the LoadEnvVars object and loads the environment variables.

        Parameters:
        ----------
        file_path : str
            The path to the environment configuration file.
        """
        self.file_path = file_path
        with open(file_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value


LoadEnvVars('conf/env.conf')

LISTEN_SERVER_IP = os.getenv('LISTEN_SERVER_IP')
LISTEN_SERVER_PORT = int(os.getenv('LISTEN_SERVER_PORT'))