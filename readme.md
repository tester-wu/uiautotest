<<<<<<< HEAD
# 自动化测试框架文档（基于 Playwright + Pytest + Allure）

## 一、框架目标
- **零代码门槛**：测试团队直接使用 Playwright 录制脚本，仅需维护 YAML 数据文件  
- **高可维护性**：元素定位和测试数据分离，页面变动时只需修改配置文件  
- **标准化流程**：统一测试环境初始化、报告生成和日志管理  


## 二、项目结构AutomationTesting/
├── config/                  # 配置中心（测试团队可修改）
│   ├── config.yaml          # 环境配置（基础URL、浏览器参数）
│   └── logging.yaml         # 日志配置（格式/存储路径）
├── data/                    # 数据中心（核心维护点）
│   ├── test_data/           # 测试数据（YAML格式，按场景分组）
│   │   └── login_data.yaml  # 登录场景数据（用户名/密码等）
│   └── page_elements/       # 页面元素定位（YAML格式，按页面分组）
│       └── login_page.yaml  # 登录页面元素选择器（Playwright语法）
├── tests/                   # 测试用例（录制脚本直接存放）
│   ├── test_example.py      # Playwright录制的测试脚本（核心用例）
│   ├── conftest.py          # pytest夹具（自动初始化浏览器/页面）
│   └── test_utils/          # 测试辅助工具（测试团队可简单调用）
│       ├── data_reader.py   # 测试数据读取工具（读取data/test_data/文件）
│       └── element_locator.py # 元素定位工具（读取data/page_elements/文件）
├── core_utils/              # 核心工具（开发维护，测试团队不修改）
│   ├── browser_manager.py   # 浏览器初始化（基于config.yaml配置）
│   ├── logging_manager.py   # 日志处理（自动生成logs/test.log）
│   └── yaml_reader.py       # YAML通用读取工具（支持所有YAML文件解析）
├── pytest.ini               # pytest配置（Allure报告路径等）
├── run_tests.py             # 一键运行脚本（执行测试+生成报告，测试团队直接用）
├── requirements.txt         # 依赖清单（环境搭建所需库）
└── README.md                # 项目说明文档

## 三、核心模块功能（测试团队关注）
### 1. 数据管理（维护成本最低）
#### 测试数据（`data/test_data/`）
- **格式**：YAML，按场景命名（如登录场景为 `login_data.yaml`）  
- **作用**：存储用户名、密码等动态数据，避免硬编码在脚本中  
- **示例**：  
  ```yaml
  # login_data.yaml
  username: ye.wu@ninebot.com  # 直接对应录制脚本中的变量名
  password: Cyber@123
  ```

#### 元素定位（`data/page_elements/`）
- **格式**：YAML，按页面命名（如登录页面为 `login_page.yaml`）  
- **作用**：存储元素选择器（支持Playwright的`get_by_*`/`locator`语法）  
- **示例**：  
  ```yaml
  # login_page.yaml
  login_button: "[role=button][name=登录]"  # 登录按钮选择器
  username_input: "text=用户帐户"           # 用户名输入框选择器（文本定位）
  ```


### 2. 测试用例（录制脚本直接使用）
- **来源**：通过 `playwright codegen` 录制生成，直接保存到 `tests/` 目录  
- **修改点**：仅需添加两行代码读取数据和元素（其他步骤保留录制结果）  
  ```python
  # test_example.py（录制后修改部分）
  from tests.test_utils.data_reader import read_test_data
  from tests.test_utils.element_locator import get_element_selector

  login_data = read_test_data("login_data.yaml")       # 读取测试数据
  username_selector = get_element_selector("login_page", "username_input")  # 读取元素定位
  ```


### 3. 一键运行（测试团队核心操作）# 1. 运行测试（自动执行所有用例）
python run_tests.py

# 2. 查看报告（浏览器自动打开）
allure open allure-report

## 四、环境搭建（首次运行必做）
### 1. 安装依赖pip install -r requirements.txt#### 依赖清单（`requirements.txt`）# 核心测试框架
pytest>=7.0            # 测试运行器
playwright>=1.30.0     # UI自动化引擎
allure-pytest>=2.13.2   # 报告生成工具

# 辅助工具
pyyaml>=6.0            # YAML解析器
### 2. 初始化浏览器驱动playwright install（自动安装Chromium/webkit/firefox驱动，默认使用Chromium）


## 五、维护指南（测试团队重点）
### 1. 新增测试场景
1. **录制脚本**：使用 `playwright codegen 目标URL` 录制新场景，保存为 `tests/test_xxx.py`  
2. **创建数据文件**：在 `data/test_data/` 新建 `xxx_data.yaml`，填写动态数据  
3. **创建元素文件**（可选）：若元素需统一维护，在 `data/page_elements/` 新建 `xxx_page.yaml`  
4. **修改脚本**：仅添加数据和元素读取代码，其他步骤保留录制结果  

### 2. 元素定位变更
- **场景**：页面改版导致按钮/输入框定位变化  
- **操作**：直接修改 `data/page_elements/对应页面.yaml` 中的选择器，无需改动测试脚本  

### 3. 环境切换
- **场景**：切换UAT/生产环境，或修改浏览器参数（如无头模式）  
- **操作**：修改 `config/config.yaml` 中的 `base_url` 和 `browser` 配置  


## 六、团队分工建议
| 角色           | 负责模块                 | 操作说明                          |
|----------------|--------------------------|-----------------------------------|
| 测试工程师     | data/目录、tests/脚本    | 录制脚本、维护YAML数据/元素文件    |
| 开发工程师     | core_utils/、run.py      | 维护底层工具、框架升级            |
| 所有人         | config/目录              | 修改环境配置（如基础URL）          |


## 七、常见问题
### 1. 录制脚本无法运行？
- 检查 `conftest.py` 中的 `page` fixture 是否正确注入  
- 确认 `config/config.yaml` 中的 `base_url` 与录制脚本中的URL一致  

### 2. 元素定位失败？
- 打开 `data/page_elements/对应页面.yaml`，使用Playwright Inspector验证选择器  
- 优先使用 `get_by_role`/`get_by_text` 等语义化选择器，避免脆弱的XPath/CSS  


通过此框架，测试团队可在保留录制脚本原生语法的同时，实现数据和元素的标准化维护，大幅降低后期脚本修改成本。核心逻辑通过YAML文件管理，真正实现“零代码”维护。    


1、测试用例名称规范
2、报告增加录屏以及失败截屏
3、报告增加mark装饰符使得更完善


git init                                                                 #初始化本地仓库，本地生成一个.git文件
git remote add origin https://gitlab.com/ui-autotest/uiautotest.git      #远程仓库链接
git pull origin master                                                   #拉取远程仓库文件
git add .                                                                #将文件添加到暂存区
git commit -m "Add ."                                                    #将暂存区的文件提交到本地仓库
git push origin master                                                   #将本地仓库的文件推送到远程仓库
