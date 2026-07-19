# 10007 MRS Updater

每12小时从 `lingeringsound/10007_auto` 获取 hosts，验证不少于10000个域名，转换并反向校验 `dist/10007-Ads.mrs`。只有内容变化时才提交。

发布后在 Mihomo 中使用：

```yaml
type: http
behavior: domain
format: mrs
url: https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/dist/10007-Ads.mrs
interval: 43200
```
