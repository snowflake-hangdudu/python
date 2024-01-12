# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

import scrapy
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BaiduSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class BaiduDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.meta['proxy'] = '121.41.122.240'
        if spider.name == 'szuSearch':
            # 请求头
            header = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/120.0.0.0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
            }
            request.headers.update(header)

        # 抖音头
        if spider.name == 'douyinp':
            header = {
                'Cookie': 'n_mh=otMAA3zkSJ5_qW0REg7q9om7j8nNXGXFAXzLBrXvtbc; store-region=cn-gd; store-region-src=uid; xgplayer_user_id=671166125483; LOGIN_STATUS=1; ttwid=1%7C2bgZWMqjiospJcjPh-BHA14_56PzcTyDvvUbQ1hqJdo%7C1700624720%7Ccd3236d5b6ff9ce055a15b9106e9c1c99467575a5c9af992b940103287364b85; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; csrf_session_id=cda80acf8fddac3a79a1bbb4cc0b005c; s_v_web_id=verify_lqyperr1_uUHmvLJi_lrom_4OlI_8azj_0K5t97WeV1Uo; passport_csrf_token=a1dcc621fe776c28e91090ff564700b6; passport_csrf_token_default=a1dcc621fe776c28e91090ff564700b6; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; bd_ticket_guard_client_web_domain=2; sso_uid_tt=2ea45855e433fb0cc07bea432be160ef; sso_uid_tt_ss=2ea45855e433fb0cc07bea432be160ef; toutiao_sso_user=44adeb769e29054e3c1aa94fdf0e2349; toutiao_sso_user_ss=44adeb769e29054e3c1aa94fdf0e2349; passport_assist_user=CkFR1mTykX1HJQyoTyRpbrAFzsbAukJI2vymiuGKfbn29IYRFY_1tUgMVZoNkA0Z2wfI_GSqreC2YUfWmzKKwSgN1BpKCjwk7Ahr9BndEbBSDawcPFEQ_b4yWSLbTDMYRBIPPtl75IaxbGycMhgQ9dGIwxx-tlSqQdbRW2brgeRez1YQ797FDRiJr9ZUIAEiAQP3hS0A; sid_ucp_sso_v1=1.0.0-KGY2MTM1YzJhY2U0ZTRkY2I2M2UzY2FhM2ZlMTlkMGRjMWZlODUyOGUKHwitg4Cjr_SWBRDQ5tisBhjvMSAMMPaNvekFOAZA9AcaAmxxIiA0NGFkZWI3NjllMjkwNTRlM2MxYWE5NGZkZjBlMjM0OQ; ssid_ucp_sso_v1=1.0.0-KGY2MTM1YzJhY2U0ZTRkY2I2M2UzY2FhM2ZlMTlkMGRjMWZlODUyOGUKHwitg4Cjr_SWBRDQ5tisBhjvMSAMMPaNvekFOAZA9AcaAmxxIiA0NGFkZWI3NjllMjkwNTRlM2MxYWE5NGZkZjBlMjM0OQ; passport_auth_status=c60f05d382e9f450962a444d82ad3a24%2C; passport_auth_status_ss=c60f05d382e9f450962a444d82ad3a24%2C; uid_tt=28787661ea6a48b7383c6c50b2317e98; uid_tt_ss=28787661ea6a48b7383c6c50b2317e98; sid_tt=81ba9eb4be7eee0b4f3531fbef2f9da8; sessionid=81ba9eb4be7eee0b4f3531fbef2f9da8; sessionid_ss=81ba9eb4be7eee0b4f3531fbef2f9da8; publish_badge_show_info=%220%2C0%2C0%2C1704342353805%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=04406fd18b2dee4f7c59ccc131f07bda; __security_server_data_status=1; sid_guard=81ba9eb4be7eee0b4f3531fbef2f9da8%7C1704342355%7C5184000%7CMon%2C+04-Mar-2024+04%3A25%3A55+GMT; sid_ucp_v1=1.0.0-KDYyZjNkODlmMDgyMDE1YjQ4ZGMxMjE1YmYyYjAyYzkzZmQxMGViZDUKGwitg4Cjr_SWBRDT5tisBhjvMSAMOAZA9AdIBBoCbHEiIDgxYmE5ZWI0YmU3ZWVlMGI0ZjM1MzFmYmVmMmY5ZGE4; ssid_ucp_v1=1.0.0-KDYyZjNkODlmMDgyMDE1YjQ4ZGMxMjE1YmYyYjAyYzkzZmQxMGViZDUKGwitg4Cjr_SWBRDT5tisBhjvMSAMOAZA9AdIBBoCbHEiIDgxYmE5ZWI0YmU3ZWVlMGI0ZjM1MzFmYmVmMmY5ZGE4; __live_version__=%221.1.1.6845%22; live_can_add_dy_2_desktop=%220%22; live_use_vvc=%22false%22; webcast_leading_last_show_time=1704342363391; webcast_leading_total_show_times=1; webcast_local_quality=origin; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.225%7D; strategyABtestKey=%221704419933.276%22; __ac_signature=_02B4Z6wo00f01va8xlwAAIDD.Jod9.iCtHr2nMLAANhFWBNfp-h5bCJh85oY-6SHgfN2shFR8MShKGq1fHp8jW1tMnldKEJj5qTlkQV2C9yo2MuVbLOMcKFKwdVKiKgbtRvp77f5o1SoTNud8e; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20240104%2F1%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA9zXT6z_WYqjEPovagT8JLc6977RyEZamOa3QQqNvlimmSSmJlJc9CWAdKVhbM0dv%2F1704470400000%2F0%2F0%2F1704440974069%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA9zXT6z_WYqjEPovagT8JLc6977RyEZamOa3QQqNvlimmSSmJlJc9CWAdKVhbM0dv%2F1704470400000%2F0%2F0%2F1704441574070%22; odin_tt=3d278a9678dd0d9c4b227f0fd9ee6536b678171b2c509a5c81ec5e978568a408238d8de4557d6af0d8d5dda0eb83d46a; tt_scid=H3bq9hjhZIBfNu.M1yrksVGqWe8tseyDDOD8oR6AUMlhRgc8sA8o4yojBizRRPdB33d1; xg_device_score=7.802204888412783; pwa2=%220%7C0%7C3%7C0%22; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ2Q0N1Fpc3ZVTzJpanNnVFRKZDh1V2tRNE5PVElRVGZHaHNlMzV0UUhIaDEzblo5bGY1N3RtWDh5M21hS0l5YWkxdXEvV3huQ0wvUjJ5NHRJQWlBUVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=e9YM36v0JqugX5ZQNVFe3mQUi09cP10WM-1py64daypvqL5I89EvvCPlK1aJ-ywUc0w59kZX2MQNzlKWXKyIsUSc1x9QAlEXtCtIiQezHGj71hTklQuId8NluWqru5o=; msToken=QxAJWYnehG_F7mteJZRiixwIk5MDefxbkGBbyNTCziq1MHS-jKP9cYpY9cnXQXHI5TNVNv_YLB08OSXXUsp8ecPQVyQapvmDnKvITuE1jiosAP8E_dYBZ1orGP87KLw=',
                'Accept': 'application/json, text/plain, */*',
                'Host': 'www.douyin.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Referer': 'https://www.douyin.com/hot',
                'Connection': 'keep-alive'
            }
            request.headers.update(header)
        # 快手头
        elif spider.name == 'kuaishoup':
            header = {
                'Cookie': 'kpf=PC_WEB; clientid=3; did=web_b8c48a2e27ccfedd77ea1d8f96bd7a23; didv=1704787043883; kpn=KUAISHOU_VISION',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Host': 'www.kuaishou.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Referer': 'https://www.kuaishou.com/brilliant',
                'Connection': 'keep-alive'
            }
            request.headers.update(header)
        elif spider.name == 'zhihup':
            header = {
                'Accept': '*/*',
                'Host': 'www.zhihu.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
                'Referer': 'https://www.zhihu.com/hot',
                'Connection': 'keep-alive',
                'Cookie': 'd_c0="ABAQVrfcpxOPTjbdC6GQqTUHDg45eyWo4_E=|1630462554"; YD00517437729195%3AWM_TID=2VwO3jHPfo1EBVRBQEbUlNatRYZUPxCI; _xsrf=XyZf9yTb9ty24QCrDeA2fNsHwA3k2cyz; YD00517437729195%3AWM_NI=fIQnoWQl%2FbsiQ%2F%2BnUMXRV4eFkKRSsFDUviEljiYpEwdgFHYTHUXZiliQLrb1wbSkYxf6qA1daZbgDR6gEv%2FRkdmEfnaFu7fsOxboPXqiVQXRgMbZOShroT%2BdF7QiH%2Bdkckc%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6ca54ae98af94e954f1ac8bb2d14f829e8b83d57da1a6a2b5f040a5ae88b8c52af0fea7c3b92aa6979f8fee5d93b4e183f26393f1e58fd8479c8e9ad5e84ea9959eb4f24e888bba8ac868aab79791c87da8b98aa9dc608c8b98bbec68ab8f8493e13bb5be9d8cdc74a6eabfa2b470a386ae88c75af6b98b97ae5aa9bca3a6e566a39abbd8e5798da8ae90d354b3b79ab2db5aa593aebbce59acaea1b5aa7086e99f8acb21a8b5ad8ce237e2a3; __snaker__id=UMVvm1gH85B9NV8N; q_c1=8c62ba83336b4e97a59b96ba7a3fb97d|1686533325000|1686533325000; _zap=2c4ce9c9-18e6-4bed-b660-22f23c2b155c; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1704355161; BAIDU_SSP_lcr=https://www.bing.com/; gdxidpyhxdE=vc9CKQpmwhzX9DdsVmE2mS%2B0%5CA3q7t0RwhXsExCePkXA%2BUNK8Y4N26IirZnMf4uCvfVegp%5CibeQMcVx9fwILP%2BBXlaurCEYyepd1l3VPmIS49zQYj4ds74ktKhwnBrMvE%5Co6BXDiU4VwM%2FDv%5CPLJ9x0atWMZbyTz2Ze9JvfOYTxwWoPW%3A1704697498229; captcha_session_v2=2|1:0|10:1704696628|18:captcha_session_v2|88:OXAwNWNqcTcxK0F2a1RyRFlML1lVc2tkWUVjSk1leWc1bjlMRURTNDg4eWFSekhPVXR6RFRqU2JnaFJrcmNPcw==|eefb2f030255cf8fc856e8c705e36b2270f0709a02a33213d42b8d760592bd91; captcha_ticket_v2=2|1:0|10:1704696676|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfUVlSaU8zV18qem81dW40X3U4ZVIxNWRLUmlLKkFFZVowNXFYb2k2aGw1THRWVWlCU0hyYk5ZMzJndGlGUUJuVCpmbVhmYU8xWW1COGl2NGNqYTVaKno4MldqOGdpeWlwbERreGhlV0ZWdFJoMHQyeWtBbjBzNDhjTTZBZ0RVWkVwZypVMk1pZlFmTjhGLnZhR2pnNEdMSmpzczZWTEt6S0pxQXVGOXZXT3Z1OCpFSl9BSF9ONFAyYThvY0xYQ0Z0dE92UFk2d1RRa0JLRktlYXZWTnNwSjhaMkdyYkIyNE85MWVybXhwNWxhRkpVa1AxV0kwSUo1bmJIY3cxMnhqYW1LZkQwZ01HYl9acSo5RkhxUmRYR2YzampyalYqNFdNaHZTbTAwak1YWkdoZlNWWnRfdW1XZzNKU1JqallCZE9nbnVJcWhzOUF0eG9qVUZCNWJFbmZZb0tsSi5Qa2FyZnA4a2ZhSUxBMzRwcDZYOVZmb2dsdDVYbXZoSnZhQW13SlhHWGdpVWFzdDFNRVpxTWZyS2JwNWpNRkZDMElpalk4OGZGa1k1ZGp3Tm13SnlOVDF4ZUtaS3p6cEhFcG9tcENza1dlR01sZU9veUNZNncqUkdzQV9zOUZCVzR0aWhIZF9oaHRtRlNRVjNfSkVvVUtkLjRpTG5DdVE4cnZTZTBweG9nNVg3N192X2lfMSJ9|b0516350b3182052fbd8fb1b99a7bc7524ef18568959328f03b9c591c97ff213; z_c0=2|1:0|10:1704696695|4:z_c0|92:Mi4xLUlCUUF3QUFBQUFBRUJCV3Q5eW5FeVlBQUFCZ0FsVk5kLW1JWmdEbnpfbmY2TXlRNTFQMkRDTWlKUXNrd0VnejRB|0a27d735c83d3034c28f9267161c9512fb4a2b3f1cdc8db478eb93d504d4a9cc; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1704780047; SESSIONID=Lg5KpIq3QngvbfanGemt32Ds8eAxmw3OOw6tpxQeXlP; JOID=U1ARB0xdv0An7cYXDlgwXT8CVv8dGNR1b5uGaj0K2CtRjKZ_bEhS30fiwxsNaWEhISRhPNw00iVNG2GzEOVSVD0=; osd=UFEUCkJevkUq48UWC1U-Xj4HW_EeGdF4YZiHbzAE2ypUgah8bU1f0UTjxhYDamAkLCpiPdk53CZMHmy9E-RXWTM=; KLBRSID=ca494ee5d16b14b649673c122ff27291|1704780058|1704778749',
            }
            request.headers.update(header)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
