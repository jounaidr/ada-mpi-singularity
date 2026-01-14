from openapi_client import SlurmApi
from openapi_client import SlurmdbApi
from openapi_client import ApiClient as Client
from openapi_client import Configuration as Config

from openapi_client import V0040JobSubmitReq
from openapi_client import V0040JobDescMsg

config = Config()
config.host = "http://172.16.114.98:6820/"
config.access_token = "SLURM_JWT_TOKEN"

slurm = SlurmApi(Client(config))
slurmdb = SlurmdbApi(Client(config))

refl1d_job = V0040JobSubmitReq(script="#!/bin/bash\nsrun singularity exec --bind /home/ubuntu/slurm-test:/test /home/ubuntu/slurm-test/mpi4py-mpich-refl1d.sif refl1d /test/Ni58_basic_model.py --fit=dream --export=test --burn=1000 --samples=10000 --init=lhs --mpi --session=/test/test.h5 --batch",
                               job=V0040JobDescMsg(
                                   name="openapi-test",
                                   ntasks=1,
                                   current_working_directory='/home/ubuntu/slurm-test',
                                   standard_input="/dev/null",
                                   standard_output="/home/ubuntu/slurm-test/refl1dTest-%j.out",
                                   standard_error="/home/ubuntu/slurm-test/refl1dTest_error-%j.out",
                                   environment=['PATH=/bin/:/sbin/:/home/slurm/bin/:/home/slurm/sbin/']
                               ))

response = slurm.slurm_v0040_post_job_submit(refl1d_job)
print(refl1d_job)
