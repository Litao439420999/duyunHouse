from wordcloud import WordCloud
import jieba
import imageio


"""都匀出租房数据词云"""
# 基础配置数据
filename = "anjuke-m1041.csv"
backpicture = "resources\\house2.jpg"
savepicture = "resources\\都匀出租房数据词云.png"
fontpath = "resources\\simhei.ttf"
stopwords = ["null", "暂无", "数据", "上传", "照片", "房本"]

# 读入数据文件
comment_text = open(filename, encoding="gbk").read()   #"utf-8"
# 读取背景图片
color_mask = imageio.imread(backpicture)

# 结巴分词,同时剔除掉不需要的词汇
ershoufang_words = jieba.cut(comment_text)
ershoufang_words = [word for word in ershoufang_words if word not in stopwords]
cut_text = " ".join(ershoufang_words)

# 设置词云格式
cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path=fontpath,
    # 设置背景色
    background_color='white',
    # 词云形状
    mask=color_mask,
    # 允许最大词汇
    max_words=2000,
    # 最大号字体
    max_font_size=60
)
# 产生词云
word_cloud = cloud.generate(cut_text)
# 保存图片
word_cloud.to_file(savepicture)