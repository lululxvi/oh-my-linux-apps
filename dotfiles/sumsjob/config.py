# the host name of the local area network to access the servers
# None if not required
LAN = None
# server host names
servers = [
    "apma-gpu-06",
    "apma-gpu-07",
    "saluzi",
    "apma-gpu-04",
    "apma-gpu-03",
    "apma-gpu-05",
    "apma-gpu-02",
    "apma-gpu-01",
    "dilu",
    "wuzhui",
    "chitu",
    "jueying",
]

# GPUs to be excluded
# e.g., gpus_exclude = ["Quadro"] to exclude all GPUs whose name contains "Quadro"
gpus_exclude = ["Quadro"]

# the root folder to run your job
path_prefix = "~/scratch"

# the command to run your job
cmd = "/opt/anaconda3/bin/python"

# options for [rsync](https://linux.die.net/man/1/rsync)
# files required to run the job, i.e., files will be pushed to the server
files_push = "--include='[^.]*/' --include='*.py' --exclude='*'"
# new files you need, i.e., files will be pulled back from the server
files_pull = "--include='*.dat' --include='*.log' --exclude='*'"
