这是一个爬取招聘网站信息的分布式爬虫项目

- spiders文件夹下共有6个爬虫文件,分别是对6个招聘网站的爬取,均是全站爬取;job1,请求头cookie需登录账号在页面中查看后填写（后来发现拉勾不用cookie也可以）

- 几个main文件是对爬虫文件的执行,可以同时多开

- settings中需要再设置redis服务器的地址,使用scrapy_redis实现redis缓存,过滤,避免爬取重复页面,可以实现分布式爬虫

- 数据可以边抓取边存入MySQL中,也可先存入redis中,后续再从redis中取出存入MySQL,需设置选择不同的pipeline
