# About

Simple backend and front-end application that illustrates simple web architecture.

## Authors

- [@artemd](https://www.github.com/artemd)


## Screenshots

TBD


## Deployment

In order to deploy backend application you need to build a docker image:

```shell
docker build . -t cloudtest
```

Running application from a built image is easy:

```shell
docker run -d -p 8080:8080 cloudtest
```

## Run Locally

In order to run program locally please install requirements first:

```shell
pip install pipenv
cd backend
pipenv install
```

Running flask development server

```shell
cd backend
pipenv shell
python app.py
```

## Support

For support contact ArtemD on GitHub.

# License

[MIT](https://opensource.org/licenses/MIT)