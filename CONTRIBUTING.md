# 参与贡献 / Contributing

简体中文 | [English](#english)

感谢你帮助完善这个列表！

## 如何推荐数据源

请使用 [issue 模板](https://github.com/akfamily/awesome-data/issues/new/choose)提交，中文或英文均可。维护者审核通过后会将其加入列表。

## 收录标准

- **与金融或经济相关**：提供行情、财务、宏观经济、另类数据等，或者是获取这类数据的工具。
- **成熟、使用广泛**：开源项目应有一定的使用量并持续维护；产品或服务应已正式上线一段时间，并有稳定的用户群。
- **可以稳定访问**：链接能够正常打开，不需要特殊的网络环境。
- **信息真实**：简介如实描述数据内容和收费方式，不夸大宣传。
- **如实声明关联**：如果你是该数据源的开发者、运营方或员工，请在 issue 中注明。自荐不会被直接拒绝，但同样需要满足以上标准。

以下情况通常不会收录：

- 刚上线、尚无用户基础的项目
- 与金融或经济数据关系不大的服务
- 链接失效或需要付费才能查看基本介绍的页面

## 提交 PR

如果你直接提交 PR，请注意：

1. 同时更新 `README.md`（中文）和 `README.en.md`（英文），两个文件中条目的分类、顺序和链接要一致。PR 会自动运行检查脚本 `.github/scripts/check_readme_sync.py`。
2. 每个条目使用以下格式：

   ```markdown
   - [名称](https://example.com)
     - 一句话简介。
     - `免费` `中国`
   ```

3. 标签从 README 的“标签说明”中选择：费用标签（`免费`、`免费增值`、`付费`）选一个，市场标签（`中国`、`香港`、`美国`、`全球`、`加密货币`）按实际覆盖范围选择；公开数据源和商业数据源如果提供程序化访问接口，加上 `API`。英文版使用对应的英文标签。
4. 条目已停止维护或被其他产品取代时，移到“已停止维护”一节并说明原因。

---

## English

Thanks for helping improve this list!

### How to suggest a data source

Please use the [issue templates](https://github.com/akfamily/awesome-data/issues/new/choose), in English or Chinese. A maintainer will review it and add it to the list if it is accepted.

### Inclusion criteria

- **Related to finance or economics**: market, financial statement, macroeconomic or alternative data, or a tool for getting such data.
- **Well-established and widely used**: open-source projects should have real adoption and active maintenance; products and services should have been publicly available for a while with a stable user base.
- **Reliably accessible**: links should open normally without special network setups.
- **Accurate**: the description should honestly reflect the data and pricing, without marketing exaggeration.
- **Disclosed affiliation**: if you build, operate or work for the data source, please say so in the issue. Self-submissions are not rejected outright, but they must meet the same criteria.

We usually do not include:

- Newly launched projects without a user base
- Services that are not closely related to financial or economic data
- Broken links or pages that require payment to view basic information

### Pull requests

If you open a PR directly:

1. Update both `README.md` (Chinese) and `README.en.md` (English), keeping the same categories, order and links. The PR runs `.github/scripts/check_readme_sync.py` automatically.
2. Use this format for each entry:

   ```markdown
   - [Name](https://example.com)
     - A one-line description.
     - `Free` `Global`
   ```

3. Pick tags from the "Tags" table in the README: one pricing tag (`Free`, `Freemium`, `Paid`) and the market tags that match the coverage (`China`, `Hong Kong`, `US`, `Global`, `Crypto`). Add `API` to public and commercial data sources that offer programmatic access. Use the corresponding Chinese tags in `README.md`.
4. When an entry is no longer maintained or has been replaced, move it to the "Discontinued" section and explain why.
