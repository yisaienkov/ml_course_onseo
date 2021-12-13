# ml_course_onseo

```bash
> docker run -it python:3.8 /bin/bash
```

```bash
> docker build -t streamlit_service -f Dockerfile.streamlit .

> docker run -p 5000:5000 streamlit_service
```

```bash
> docker build -t fastapi_service -f Dockerfile.fastapi .

> docker run -p 8001:8000 fastapi_service
```

```bash
> docker build -t dev_ml_course -f Dockerfile.dev .

> docker run -it -v C:/ml_course_onseo/:/app/ dev_ml_course /bin/bash
```


## DVC

```bash
> dvc init

> dvc remote add -d storage gdrive://1LUer-6TYRc66rSLz7tDGixFKBRduwUd0

> dvc add resources/data.txt
```