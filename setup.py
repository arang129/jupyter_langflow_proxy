import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-langflow-proxy",
    version="0.2.0",
    url="https://github.com/bijucyborg/jupyter_langflow_proxy",
    author="DataSiens",
    description="info@datasiens.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["jupyter", "langflow", "jupyterhub", "jupyter-server-proxy"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy>=1.5.0",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "langflow = jupyter_langflow_proxy:setup_langflow",
        ]
    },
    package_data={
        "jupyter_langflow_proxy": ["icons/logo.svg"],
    },
)