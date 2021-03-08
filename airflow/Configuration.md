### Небольшой гайд по установке и конфигу Apache Airflow в Linux [![NoIco](https://www.sherpis.com/prdsite/prdsite/static/mblog/images/social/airflow.png)]()

**Apache Airflow** — один из мощных workflow менеджеров, позволяющий существенно расширить возможности в автоматизации задач современного дата инженера (Data Engineer) и дата сайентиста (Data Scientist).

### Требования к установке Apache Airflow

1. Операционная система Linux - например, Ubuntu 20.04.2 LTS.

2. База данных PostgreSQL 12.6 на Ubuntu и конфигурация БД под Apache Airflow, вместо дефолтной SQLite. Последняя также подойдет в качестве примера [[инструкция]](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

3. Установка и настройка pgAdmin 5.0 в режиме сервера [[инструкция]](https://www.digitalocean.com/community/tutorials/how-to-install-configure-pgadmin4-server-mode-ru)

4. Среда разработки - Python 3.9.2 с отдельным виртуальным окружением.

Для настройки pgAdmin 5.0 в рамках п.3  используются следующие настройки файла конфигурации config_local.py:
> **~$** nano prg_env_1/lib/python3.9/site-packages/pgadmin4/config_local.py


```
import os

DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))

LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')

SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')

SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')

STORAGE_DIR = os.path.join(DATA_DIR, 'storage')

SERVER_MODE = False
```

Для запуска pgAdmin (п.3) как вариант:

```
python3.9 prg_env_1/lib/python3.9/site-packages/pgadmin4/pgAdmin4.py
```


### Процесс установки Apache Airflow
Активируем виртуальное окружение, исходя из структуры разделов: 

```
~$ cd /home/nicholas_id/virtual_env/;

~$ source prg_env_1/bin/activate
```

> **Примечание**: смена текущей версии питона (по умолчанию)  в Ubuntu, например:

```
~$ sudo ln -fs /usr/local/bin/python3.9 /usr/bin/python3
```

После успешной подготовки среды на этапах 1-4 следует процесс установки Apache Airflow.

Для того,  чтобы избежать множества каскадных проблем (ошибок), рекомендуется посмотреть раздел [[Installation]](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/index.html)

```
Installation

On November 2020, new version of PIP (20.3) has been released with a new, 2020 resolver. This resolver does not yet work with Apache Airflow and might lead to errors in installation - depends on your choice of extras. In order to install Airflow you need to either downgrade pip to version 20.2.4 pip install --upgrade pip==20.2.4 or, in case you use Pip 20.3, you need to add option --use-deprecated legacy-resolver to your pip install command.
```

Суть в том, что предустановленный pip version 21.0.1 придется даунгрейдить до версии 20.2.4:

```
(prg_env_1)~$ pip install --upgrade pip==20.2.4
```

После данной манипуляции Apache Airflow встает, как надо:


```
(prg_env_1)~$  pip install apache-airflow
```

Возможно, также потребуется установка apache-airflow-providers-http.
Кроме того, Airflow можно ставить с зависимостями, исходя из потребностей. Например:

```
(prg_env_1)~$  pip install apache-airflow[postgres,s3]
```

Подробнее [[тут]](https://airflow.apache.org/)

Apache Airflow хранит свои настройки в
'/home/nicholas_id/airflow/airflow.cfg'. 
Для удобства можно задать переменную среды AIRFLOW_HOME:

```
~$ export AIRFLOW_HOME=~/airflow/
```

Изменения файла конфигурации airflow.cfg:

**1** Вместо SequentialExecutor используется одно из популярных в продакшн решений CeleryExecutor, меняем параметр:

> **executor** = CeleryExecutor

**2** В качестве БД для Airflow используется PostgreSQL:


> **sql_alchemy_conn** = postgresql+psycopg2://airflow:airflow@localhost:5432/airflow_metadata

где airflow - имя пользователя, airflow_metadata - имя БД.


**3** Отключаются примеры:

> **load_examples** = False

**4** Меняются broker_url и result_backend:

> **broker_url** = amqp://guest:guest@localhost:5672//

**result_backend** = amqp://guest:guest@localhost:5672//


!Далее осуществляется миграция всех сущностей Airflow в сконфигурированную ранее БД:

```
(prg_env_1)~$  airflow db init

(prg_env_1)~$  airflow db check
```

Все изменения можно также наблюдать в pgAdmin. Например, через порт 5050:
> http://127.0.0.1:5050/

Инициализия Rabbitmq-брокера для перезапуска направленных ацикличных графов DAG c [[Celery]](https://en.wikipedia.org/wiki/Celery_(software)).

Установка rabbitmq-server:

```
~$  sudo apt install rabbitmq-server
```

Конфигурационный файл располагается в:
'/etc/rabbitmq/rabbitmq-env.conf'

Меняется:

> **NODE_IP_ADDRESS**=0.0.0.0 

Запуск RabbitMQ сервиса:

```
~$  sudo service rabbitmq-server start
```

Далее устанавливается [[Celery]](https://en.wikipedia.org/wiki/Celery_(software)):

```
(prg_env_1)~$  pip install celery
```

При установке Celery необходимо следить за совместимостью версий с RabbitMQ и Airflow. 

Создание директории для DAGs:

```
~$  mkdir -p /home/nicholas_id/airflow/dags/
```

На этом основные требуемые инсталляции и конфигурирование можно считать завершенными этапами.
#
### Запуск  Airflow

Запуск всех сервисов Airflow для старта инструмента через webUI:

```
~$  airflow webserver

~$  airflow scheduler

~$  airflow celery worker
```

Если прокидывается warning о том, что нет ни одного зарегистрированного пользователя Airflow, то решается этот момент [[таким образом]](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#create_repeat1)

### Остановка  Airflow
Для остановки Airflow необходимо получить id процесса (pid) и затем завершить его.
Посмотреть pid можно либо в консоле, либо так:

```
~$  cat $AIRFLOW_HOME/airflow-webserver.pid
```

После чего вводится:

```
~$  sudo kill -17790 {process_id of airflow}
```

Далее идет процесс построения data pipeline на Apache Airflow.

#

![No image](https://www.sherpis.com/prdsite/media/posts/2021/03/04/airflow_install.png)