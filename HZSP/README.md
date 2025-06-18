# 作文评价系统：HZSP(Hanyu Zuowen Shuiping Pingjia)
本项目用于演示基于大语言模型(LLMs)调用实现的Web前端作文评价系统的工作原理。

## 功能特点
- 代码极简，适于理解原理
- 支持流式输出，实时显示评价结果
- 默认基于OpenAI SDK (稍加修改即可切换至其他模型，例如可参考[DeepSeek](https://api-docs.deepseek.com/zh-cn/))。也可使用本地模型，参考[Transformers](https://huggingface.co/docs/transformers/index)。
- 基于prompt的高度自定义评价维度(app.py中修改)
- 前端和输出语言的多语言支持，多种浏览器比例。

## 使用说明

1. 下载项目到本地
2. 安装依赖(推荐在创建新环境，python=3.12)：
   ```bash
   pip install -r requirements.txt
   ```
3. 在系统变量中添加OPENAI_API_KEY变量，加入API密钥
4. 项目路径下，启动Flask服务器：
   ```bash
   python app.py
   ```
2. 在浏览器中访问：`http://localhost:5000`

## 使用说明

1. 在左侧文本框中输入需要评价的作文
2. 点击"执行评分"按钮
3. 等待评价结果在右侧文本框中实时显示

## 注意事项

- 需要有效的API密钥
- 建议使用主流浏览器（Chrome、Edge、Safari等）访问 