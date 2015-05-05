#-*- coding: utf8 -*-
import common


def get_data_price(date, code):
    """
    일별 가격, 거래량을 수집한다.
    """
    SEED = "http://m.stock.naver.com/api/item/getPriceDayList.nhn?code={code}&pageSize={page_size}&page={page}"
    SEED = SEED.replace('{page_size}', '10')

    rv = common.base_dict()
    for page in range(1, 300):
        url = SEED
        url = url.replace('{code}', code)
        url = url.replace('{page}', str(page))
        j = common.get_json(url)
        rows = j.get('result', dict()).get('list', [])
        for row in rows:
            if row.get('dt') == date:
                rv['date'] = date
                rv['price_max'] = int(row.get('hv', 0)) # 고가
                rv['price_min'] = int(row.get('lv', 0)) # 저가
                rv['price_start'] = int(row.get('ov', 0)) # 시가
                rv['price_end'] = int(row.get('ncv', 0)) # 종가
                rv['trade_cnt'] = int(row.get('aq', 0)) # 거래량
                return rv
            if row.get('dt') < date:
                raise Exception('may be '+date+' is holiday')
    raise Exception('not found data.')



# {"result":{"list":[{"dt":"20150504","ncv":16900,"rf":"5","cv":-300,"cr":-1.74,"ov":17350.0,"hv":17600.0,"lv":16800.0,"aq":1206183},{"dt":"20150430","ncv":17200,"rf":"5","cv":-500,"cr":-2.8248587,"ov":17550.0,"hv":18050.0,"lv":17100.0,"aq":1598106},{"dt":"20150429","ncv":17700,"rf":"2","cv":150,"cr":0.8547008,"ov":17650.0,"hv":18300.0,"lv":17500.0,"aq":2370882},{"dt":"20150428","ncv":17550,"rf":"5","cv":-450,"cr":-2.5,"ov":17750.0,"hv":18100.0,"lv":17350.0,"aq":2343208},{"dt":"20150427","ncv":18000,"rf":"5","cv":-300,"cr":-1.6393442,"ov":18700.0,"hv":18850.0,"lv":17900.0,"aq":2157041},{"dt":"20150424","ncv":18300,"rf":"2","cv":200,"cr":1.1049723,"ov":18150.0,"hv":19100.0,"lv":17850.0,"aq":5236397},{"dt":"20150423","ncv":18100,"rf":"2","cv":50,"cr":0.2770083,"ov":18400.0,"hv":18550.0,"lv":17700.0,"aq":2573520},{"dt":"20150422","ncv":18050,"rf":"5","cv":-200,"cr":-1.0958904,"ov":18300.0,"hv":18650.0,"lv":17500.0,"aq":5194671},{"dt":"20150421","ncv":18250,"rf":"2","cv":1650,"cr":9.939759,"ov":17500.0,"hv":18550.0,"lv":17400.0,"aq":12219372},{"dt":"20150420","ncv":16600,"rf":"2","cv":2000,"cr":13.6986301,"ov":14400.0,"hv":16600.0,"lv":14350.0,"aq":7720526},{"dt":"20150417","ncv":14600,"rf":"5","cv":-250,"cr":-1.6835016,"ov":14800.0,"hv":14800.0,"lv":14400.0,"aq":1402963},{"dt":"20150416","ncv":14850,"rf":"5","cv":-300,"cr":-1.980198,"ov":15350.0,"hv":15700.0,"lv":14550.0,"aq":3676819},{"dt":"20150415","ncv":15150,"rf":"2","cv":100,"cr":0.6644518,"ov":15200.0,"hv":15300.0,"lv":14900.0,"aq":1334500},{"dt":"20150414","ncv":15050,"rf":"3","cv":0,"cr":0.0,"ov":15150.0,"hv":15450.0,"lv":14900.0,"aq":1964618},{"dt":"20150413","ncv":15050,"rf":"2","cv":250,"cr":1.6891891,"ov":14900.0,"hv":15250.0,"lv":14800.0,"aq":1696792},{"dt":"20150410","ncv":14800,"rf":"3","cv":0,"cr":0.0,"ov":14850.0,"hv":14900.0,"lv":14600.0,"aq":840701},{"dt":"20150409","ncv":14800,"rf":"2","cv":150,"cr":1.0238907,"ov":14800.0,"hv":15050.0,"lv":14650.0,"aq":1496996},{"dt":"20150408","ncv":14650,"rf":"2","cv":500,"cr":3.5335689,"ov":14300.0,"hv":14800.0,"lv":14200.0,"aq":1490093},{"dt":"20150407","ncv":14150,"rf":"5","cv":-50,"cr":-0.3521126,"ov":14450.0,"hv":14800.0,"lv":14100.0,"aq":1504746},{"dt":"20150406","ncv":14200,"rf":"5","cv":-100,"cr":-0.6993006,"ov":14300.0,"hv":14300.0,"lv":13950.0,"aq":687262}]},"resultCode":"success"}
#
#
# http://m.stock.naver.com/api/item/getPriceDayList.nhn?code=009830&pageSize=20&page=1
#
#
#
# code 			코드
# name 			종목명
# date			날짜
# price_max 		고가
# price_min 		저가
# price_start 	시가
# price_end 		종가
# trade_cnt		거래량
#
# {"result":{"list":[]},"resultCode":"success"}
# x = get_html('http://m.stock.naver.com/api/item/getPriceDayList.nhn?code=009830&pageSize=20&page=1')

print parse_naver('20150102', '009830')