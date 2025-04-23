import logging
import logging.config
import yaml

def setup_logger():
    """
    根据日志配置文件设置日志记录器
    :return: 配置好的日志记录器对象
    """
    try:
        # 打开日志配置文件
        with open('config/logging.yaml', 'r') as f:
            # 加载YAML格式的配置内容
            config = yaml.safe_load(f.read())
            # 根据配置内容配置日志记录器
            logging.config.dictConfig(config)
        # 获取名为test_logger的日志记录器
        return logging.getLogger('test_logger')
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error setting up logger: {e}")
        # 若出现错误，返回默认的日志记录器
        return logging.getLogger()