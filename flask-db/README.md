## 使用工厂模式创建flask application


> [The Application Factory](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/#the-application-factory)

### 创建工厂模式

    创建一个名为flaskr的python package，或者手动创建一个flaskr目录，文件内创建一个__init__.py，这样python才会把flaskr当作一个package对待。
    __init__.py中create_app方法就是工厂模式的方法。
    create_app详解参见官方文档

### 启动application

1. Linux and Mac:
    ```shell
        export FLASK_APP=flaskr
        export FLASK_ENV=developemt
        flask run
    ```

2. Windows

    ```shell
        set FLASK_APP=flaskr
        set FLASK_ENV=development
        flask run
    ```

### 访问

  浏览器访问http://127.0.0.1:5000/hello, 目前指定要了/hello。

## 配置连接数据库

> [Define and Access the Database](https://flask.palletsprojects.com/en/1.1.x/tutorial/database/)

    使用sqlite3作为数据持久化数据库。
    

指令

````
    flask init-db
````

在项目根目录下输入该指令，进行数据库初始化，它会执行提前准备好的sql文件，并生成一个instance的目录，里面会有一个
flaskr.sqlite的文件，利用pycharm Database插件选择sqlite，file选择flaskr.sqlite文件，可以直接访问数据库