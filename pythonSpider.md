# Python Spider

## Requests

## BeautifulSoup

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

- Tag
    - 遍历文档树
    - 搜索文档树
    - name
    - attribute
        - 比如`class = "boldest"`
        - 可以通过字典的方式来获取

- 其他的一些类型
    - 可浏览字符串
    - BeautifulSoup
    - Comment

###遍历文档树

`.children`

如果只要获得 Tag, 用`.contents`就可以了
或者判断

    from bs4 import element
    if type(c) == element.Tag:

? 怎么获得某个特定的attribute的tag?

A `NavigableString` is just like a Python Unicode string, except that it also supports some of the features described in Navigating the tree and Searching the tree. You can convert a `NavigableString` to a Unicode string with unicode():

3.0之后就没有unicode类型了, 直接用str就可以了吧

## Pandas

### Transfer money to number
用re模块来去掉`[$,]`, 然后转换成`float`

    df['price2'] = df.apply(lambda x: testConvert(x['price'].split(' ')[0].rstrip('+')) if x['price'][0] == '$' else 0.0, axis=1)

为什么有一个镜头的brand没有获取到?

因为这个镜头开头有空格, 所以所有的string的操作前先进行stripe比较好

### 数据的清理

删除不需要的行, 使用`boolean masking`就可以了

对列的处理


## D3 visualization
### Export data to json by pandas

    dfJson.to_json('public/pages/lens.json', orient='records')

`orient`可以输出成array of object

### Setup environment and dependencies

copy以前的d3代码

### Python http server

    python -m http.server 8080

### Test D3

    svg.selectAll('div')
        .data(rawdata)
        .enter()
        .append('div')
        .text(function d(){return d.lensName;});

### Axis

### Prime Lenses - Bubble chart

### Zoom Lenses - Bar chart
