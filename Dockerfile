FROM nvcr.io/nvidia/pytorch:23.03-py3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .isort.cfg mypy.ini .flake8 ./
COPY .ipython/ipython_config.py /root/.ipython/profile_default/ipython_config.py
COPY .ipython/00_custom_prompt.py /root/.ipython/profile_default/startup/00_custom_prompt.py

COPY my_project ./my_project
