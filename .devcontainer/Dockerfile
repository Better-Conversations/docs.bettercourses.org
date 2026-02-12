# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# ── Local cache auto-detection ───────────────────────────────────────────────
# Probes 192.168.13.3 for apt-cacher-ng (3142), Squid (3128), and Verdaccio
# (4873).  Reachable services are configured; unreachable ones are silently
# skipped so the build works on any network.
ARG CACHE_HOST="192.168.13.3"
RUN probe() { python3 -c "import socket; socket.create_connection(('$CACHE_HOST', $1), timeout=2).close()" 2>/dev/null; } \
    && if probe 3142; then \
         echo "Acquire::http::Proxy \"http://${CACHE_HOST}:3142\";" > /etc/apt/apt.conf.d/01proxy; \
         echo ">>> Configured APT cache proxy"; \
       fi \
    && if probe 3128; then \
         echo "http://${CACHE_HOST}:3128" > /tmp/.http_proxy; \
         echo ">>> Detected Squid proxy"; \
       fi \
    && if probe 4873; then \
         echo "http://${CACHE_HOST}:4873/" > /tmp/.npm_registry; \
         echo ">>> Detected NPM cache"; \
       fi

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install LaTeX (texlive-full is ~5 GB – the APT cache helps a lot here)
RUN rm -f /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y texlive-full

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN if [ -f /tmp/.http_proxy ]; then \
      export http_proxy="$(cat /tmp/.http_proxy)" https_proxy="$(cat /tmp/.http_proxy)"; \
    fi \
    && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# For developing Cloudflare Pages Functions
# RUN npm install wrangler --save-dev

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends 

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1

# Install Node and Claude
RUN if [ -f /tmp/.http_proxy ]; then \
      export http_proxy="$(cat /tmp/.http_proxy)" https_proxy="$(cat /tmp/.http_proxy)"; \
    fi \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs
RUN if [ -f /tmp/.npm_registry ]; then \
      npm config set registry "$(cat /tmp/.npm_registry)"; \
    fi \
    && npm install -g @anthropic-ai/claude-code

# Clean up cache/proxy configuration so the final image is network-agnostic
RUN rm -f /etc/apt/apt.conf.d/01proxy /tmp/.http_proxy /tmp/.npm_registry \
    && npm config delete registry 2>/dev/null || true
