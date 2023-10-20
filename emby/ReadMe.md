Emby是一款流媒体服务器软件，可以用来管理和播放媒体文件。
关于Emby更详细的信息和其他安装方式可以访问[官网](https://emby.media/)

Docker是一种容器化技术，可以让你在不同的环境中运行应用程序。

如果你想在Docker容器中运行Emby服务器，可以使用Docker Compose来定义和运行多个容器的应用程序。以下是一个Emby服务器的Docker Compose文件示例, 见docker-compose.yml文件

这个文件定义了一个服务名为emby的容器，它使用Emby服务器镜像。在这个容器中，我们将端口8096和8920映射到主机的相应端口，这样就可以从Web界面访问Emby。我们还将/config、/media和/transcode目录分别映射到主机上的三个目录，这些目录分别存储Emby服务器的配置文件、媒体文件和转码文件。最后，我们设置了一些环境变量来指定用户和组的ID。容器将在重启时自动启动，除非我们显式停止它。

要使用这个Docker Compose文件，请按照以下步骤操作：

- 将上面的Docker Compose文件保存为docker-compose.yml文件。

- 在命令行中进入包含docker-compose.yml文件的目录。

- 运行以下命令启动Emby服务器容器：docker compose up -d

- 在Web浏览器中访问http://localhost:8096，打开Emby服务器的Web界面，进行配置并添加媒体文件。注意，如果你将Emby服务器容器部署到远程服务器上，你需要使用相应的IP地址或域名来访问它。

