此为实验性质的配置。

复制yaml文件到rime家目录下。

- default.custom.yaml: 修改rime输入法列表 (我们的schema名字为`double_pinyin_wubi`)
- double_pinyin_wubi.schema.yaml: schema文件(里面引用了wubi86和zrm_wubi)。
wubi86用于反查，zrm_wubi用于定义自然码+五笔辅助码
- zrm_wubi.schema.yaml: 定义自然码+五笔辅助码的schema
- zrm_wubi.dict.yaml: 定义自然码+五笔辅助码的dict
- gen_dict.py: 生成`zrm_wubi.dict.yaml`的脚本
- data/wubi86.dict.yaml: rime-wubi包自带的五笔dict文件，用来简单的获取单字五笔的编码
- data/zrm2000.dict.yaml: `https://raw.githubusercontent.com/mutoe/rime`偷来的，修改对应的码表

生成规则：获取五笔单字的编码，然后处理zrm2000表。每一行如果编码小于等于汉字数*2，则不做修改。
否则把多余的部分移除后添加五笔辅助码(每个字取五笔编码首字母)。这种情况每个词只会处理一次。
另外对于每个汉字，添加一行五笔辅码。

