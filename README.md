其他参考：
- [Selenium Mouse API](https://selenium.dev/documentation/webdriver/actions_api/mouse)
- https://tecadmin.net/setup-selenium-with-python-on-ubuntu-debian
- https://zhuanlan.zhihu.com/p/632399597
<br>

## 使用方法
1. Fork本仓库
2. 点击Settings->Secrets and variables->Actions->New repository secret，依次配置`EMAIL`、`PASSWD`
    - EMAIL 是雀魂的邮箱账号，如有多个账户用空格分隔，例如`example@gmail.com example@qq.com`
    - PASSWD 是雀魂的密码，如有多个账户用空格分隔，与邮箱依次对应，例如`grc28r7g3 pdtaw3fwag`
3. 先在Actions页面将GitHub Action启用，再选择对应的workflow，将scheduled workflow启用
   ![enable-schedule-workflow](https://user-images.githubusercontent.com/90035785/224888848-be15ba52-1892-4a2b-9cef-b321b9a25165.jpg)
4. Enjoy it!
