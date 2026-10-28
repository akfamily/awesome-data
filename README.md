# Awesome-data

简体中文 | [English](README.en.md)

常用的金融与经济数据工具和数据源合集。

> 欢迎推荐你常用的数据源！请在本仓库[提交 issue](https://github.com/akfamily/awesome-data/issues/new/choose)，中文或英文均可，详见[参与贡献](#参与贡献)。

## 目录

- [标签说明](#标签说明)
- [开源数据工具](#开源数据工具)
- [金融数据 SDK](#金融数据-sdk)
- [公开数据源](#公开数据源)
- [商业数据源](#商业数据源)
- [已停止维护](#已停止维护)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

## 标签说明

| 标签 | 含义 |
| --- | --- |
| `免费` | 免费使用，部分需要注册 |
| `免费增值` | 有免费额度，更多数据或调用次数需要付费 |
| `付费` | 需要购买，可能提供试用 |
| `API` | 提供程序化访问接口；开源数据工具和金融数据 SDK 本身就是编程接口，不另标注 |
| `中国` `香港` `美国` `全球` `加密货币` | 主要覆盖的市场或数据范围 |

## 开源数据工具

- [AKShare](https://github.com/akfamily/akshare)
  - 优雅、简洁的 Python 财经数据接口库。
  - `免费` `中国` `全球`

- [Tushare](https://tushare.pro)
  - 中国金融数据 Python 接口，需注册，按积分开放数据权限；[旧版开源库](https://github.com/waditu/tushare)已不再维护。
  - `免费增值` `中国`

- [Yfinance](https://github.com/ranaroussi/yfinance)
  - 从雅虎财经（Yahoo! Finance）下载行情数据的 Python 库。
  - `免费` `全球`

- [Pandas-datareader](https://pandas-datareader.readthedocs.io/)
  - 为 pandas 提供远程数据访问的 Python 库。
  - `免费` `全球`

- [Wbdata](https://github.com/OliverSherouse/wbdata)
  - 访问世界银行数据的 Python 库。
  - `免费` `全球`

- [CCXT](https://github.com/ccxt/ccxt)
  - 统一接入上百家加密货币交易所行情和交易接口的开源库，支持 Python、JavaScript 等语言。
  - `免费` `加密货币`

- [Nasdaq Data Link](https://data.nasdaq.com/)
  - 纳斯达克旗下的金融与经济数据平台，前身为 Quandl。
  - `免费增值` `全球`

- [Financial Data](https://financialdata.net/)
  - 股票市场与财务数据 API。
  - `免费增值` `全球`

## 金融数据 SDK

- [WindPy](https://www.wind.com.cn/)
  - 万得（Wind）金融终端数据的官方 Python SDK。
  - `付费` `中国`

- [JQData](https://github.com/JoinQuant/jqdatasdk)
  - [聚宽（JoinQuant）](https://www.joinquant.com/help/api/help?name=JQData)数据库的官方 SDK。
  - `免费增值` `中国`

- [RQData](https://www.ricequant.com/doc/rqdata/python/)
  - [米筐（RiceQuant）](https://www.ricequant.com/welcome/)面向机构的商业 Python 金融数据工具包。
  - `付费` `中国`

- [TQSDK](https://github.com/shinnytech/tqsdk-python)
  - 信易科技（shinnytech）的 SDK，可免费获取期货 Tick 和分钟数据。
  - `免费增值` `中国`

## 公开数据源

- [国家统计局](https://data.stats.gov.cn/)
  - 中国官方宏观经济统计数据，包括 GDP、价格指数、工业、人口等。
  - `免费` `中国`

- [中国人民银行调查统计](https://www.pbc.gov.cn/diaochatongjisi/116219/index.html)
  - 货币供应量、社会融资规模、金融机构信贷收支等金融统计数据。
  - `免费` `中国`

- [商务数据中心](https://data.mofcom.gov.cn/index.shtml)
  - 免费获取中国商务部发布的数据。
  - `免费` `中国`

- [上海证券交易所](https://www.sse.com.cn/)
  - 沪市上市公司公告、行情和市场统计数据。
  - `免费` `中国`

- [深圳证券交易所](https://www.szse.cn/)
  - 深市上市公司公告、行情和市场统计数据。
  - `免费` `中国`

- [巨潮资讯](https://www.cninfo.com.cn/)
  - 中国证监会指定的信息披露网站，可查询沪深北上市公司公告和定期报告。
  - `免费` `中国`

- [新浪财经](https://finance.sina.com.cn)
  - 中国金融数据，涵盖股票、期货、期权、基金等。
  - `免费` `中国`

- [东方财富](https://data.eastmoney.com/center)
  - 中国金融数据，涵盖股票、期货、期权、基金等，用户生成的文本数据尤为丰富。
  - `免费` `中国`

- [中国指数研究院](https://www.cih-index.com)
  - 中国房地产价格数据。
  - `免费增值` `中国`

- [披露易（HKEXnews）](https://www.hkexnews.hk/)
  - 香港交易所的信息披露平台，可查询港股上市公司公告和权益披露。
  - `免费` `香港`

- [Webb Database](https://webb-database.com/)
  - 香港上市公司、董事、持股（CCASS）及公司治理数据。
  - `免费` `香港`

- [FRED（美联储经济数据）](https://fred.stlouisfed.org)
  - 免费获取美国圣路易斯联邦储备银行发布的经济数据。
  - `免费` `API` `美国`

- [SEC EDGAR](https://www.sec.gov/edgar/search/)
  - 美国证券交易委员会（SEC）的电子披露系统，可查询美国上市公司财报和公告。
  - `免费` `API` `美国`

- [Adanos](https://adanos.com/)
  - 股票市场情绪 API，信号来自 Reddit、X（FinTwit）、财经新闻和 Polymarket。
  - `免费增值` `API` `美国`

- [英为财情（Investing）](https://cn.investing.com)
  - 提供免费的实时行情、投资组合、走势图、财经新闻和股市数据等。
  - `免费` `全球`

- [世界银行公开数据](https://data.worldbank.org.cn)
  - 免费获取世界银行数据。
  - `免费` `API` `全球`

- [IMF 数据](https://data.imf.org/)
  - 国际货币基金组织（IMF）发布的各国宏观经济、国际收支和汇率数据。
  - `免费` `API` `全球`

- [OECD 数据](https://data-explorer.oecd.org/)
  - 经济合作与发展组织（OECD）发布的成员国经济、社会统计数据。
  - `免费` `API` `全球`

- [FXMacroData](https://fxmacrodata.com/)
  - 覆盖 18 种货币的宏观经济数据发布、发布日历、外汇即期汇率和 CFTC 持仓报告（COT）数据。
  - `付费` `API` `全球`

## 商业数据源

- [CSMAR](https://www.csmar.com/)
  - 深圳希施玛数据科技有限公司从学术研究需求出发，借鉴 CRSP、COMPUSTAT、TAQ、THOMSON 等权威数据库的专业标准，结合中国实际国情开发的经济金融研究型精准数据库。
  - `付费` `中国`

- [CNRDS](https://www.cnrds.com)
  - 中国研究数据服务平台，是高质量、开放式、平台化的中国经济、金融与商学研究综合数据平台。
  - `付费` `中国`

- [RESSET](https://www.resset.com)
  - 为模型检验、投资研究等提供专业服务的数据平台，高频数据比较丰富。
  - `付费` `中国`

- [萝卜投研](https://robo.datayes.com)
  - 通联数据股份公司开发的投研数据平台。
  - `免费增值` `中国`

- [ChinaScope](https://www.chinascope.com.cn)
  - 数库科技长期致力于在金融及产业领域提供基于产业逻辑的智能数据产品及系统服务，为金融机构、企业及政府部门提供数字化转型数据解决方案。
  - `付费` `中国`

- [CnOpenData](https://www.cnopendata.com)
  - 汇聚了大量互联网数据，适合查找小众或另类数据。
  - `付费` `中国`

- [预测者网](https://www.yucezhe.com)
  - 提供股票和加密货币的低、中、高频数据，以及财务数据。
  - `付费` `中国` `加密货币`

- [米筐量化平台](https://www.ricequant.com/welcome/datahub)
  - 提供股票、期货、期权等产品的行情和因子数据。
  - `付费` `中国`

## 已停止维护

以下条目已无法正常使用或已被其他产品取代，仅作记录。

- [Investpy](https://github.com/alvarobartt/investpy)
  - 用 Python 从 Investing.com 获取金融数据。因网站接口变化已无法正常使用，作者推荐改用 [investiny](https://github.com/alvarobartt/investiny)。

- [BankScope](https://www.bvdinfo.com)
  - 欧洲金融信息服务商 BvD 与银行业权威评级机构惠誉共同开发的银行业信息库。BankScope 已于 2016 年底停止服务，由 BvD 的 BankFocus（原名 Orbis Bank Focus）取代；BvD 已于 2017 年被穆迪（Moody's）收购。

## 参与贡献

推荐数据源请使用 [issue 模板](https://github.com/akfamily/awesome-data/issues/new/choose)，收录标准和提交 PR 的要求见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)
