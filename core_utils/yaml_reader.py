import yaml

def read_yaml(file_path):
    """
    读取指定路径的YAML文件并解析
    :param file_path: YAML文件的路径
    :return: 解析后的YAML数据字典，若出现错误返回None
    """
    try:
        # 以只读模式打开YAML文件
        with open(file_path, 'r', encoding='utf-8') as file:
            # 使用yaml.safe_load解析文件内容
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file: {e}")
    return None