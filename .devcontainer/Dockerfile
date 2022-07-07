FROM python:3.10.5-buster

RUN apt-get update 
RUN pip install poetry

RUN apt-get update && apt-get install --no-install-recommends -y \
    vim
#
# Add dev user with no root rights
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

#
# Add oh my zsh
RUN apt-get update && apt-get install --no-install-recommends -y \
  zsh \
  wget \
  fonts-powerline \
  curl \
  locales \
  # set up locale
  && locale-gen en_US.UTF-8
#
# Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/zsh --uid $USER_UID --gid $USER_GID -m $USERNAME
#SET HOME DIR
ENV HOME /home/$USERNAME
# generate locale for agnoster
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && /usr/sbin/locale-gen
# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
# the user we're applying this too (otherwise it most likely install for root)
USER $USERNAME
# Set XTERM
ENV TERM xterm
# Set the default shell to bash rather than sh
ENV SHELL /bin/zsh
 # run the installation script  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#RUN git clone --depth 1 git://github.com/zsh-users/zsh-completions.git $HOME/.oh-my-zsh/custom/plugins/zsh-completions
RUN cd $HOME && curl -fsSLO https://raw.githubusercontent.com/romkatv/dotfiles-public/master/.purepower
ADD agnoster.zsh-theme $HOME/.oh-my-zsh/themes
# zsh configuration
ADD .zshrc $HOME
#
# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog