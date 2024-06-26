if status is-interactive
    # Commands to run in interactive sessions can go here
    set -x PATH $PATH $HOME/.local/bin
    set -x LD_LIBRARY_PATH $LD_LIBRARY_PATH /opt/anaconda3/lib
    set -x XLA_FLAGS "--xla_gpu_cuda_data_dir=/opt/anaconda3"

    alias rm="rm -i"
    alias gitpullall="find . -type d -name .git -print -execdir git pull \;"
    alias gitstatusall="find . -type d -name .git -print -execdir git status \;"
end
