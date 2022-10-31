from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/sgoodm/test",
    #access_token=<my_access_token> # only required for private repos
)
block.get_directory("flows") # specify a subfolder of repo
block.save("dev")



"""

prefect deployment build dataset_abc/healthcheck.py:healthcheck --name dataset_abc --tag dataset --work-queue geodata --storage-block github/dev

prefect deployment apply healthcheck-deployment.yaml

prefect deployment run healthcheck/dataset_abc

"""


import configparser

config = configparser.ConfigParser()
config.read('config.ini')
name = config["main"]["name"]

from healthcheck import healthcheck
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

storage = GitHub.load("dev") # load a pre-defined block

deployment = Deployment.build_from_flow(
    flow=healthcheck,
    name="dataset_abc_test1",
    version=1,
    work_queue_name="dataset",
    storage=storage,
    parameters={'name':name}
)

deployment.apply()