package com.alipay.run;

import com.alipay.api.AlipayApiException;
import com.alipay.api.AlipayClient;
import com.alipay.api.DefaultAlipayClient;
import com.alipay.api.domain.AlipayTradeWapPayModel;
import com.alipay.api.request.AlipayTradePagePayRequest;
import com.alipay.config.AlipayConfig;

public class AliPayDemo {

	public static void main(String[] args) throws AlipayApiException {
		// 调用RSA签名方式
		AlipayClient client = new DefaultAlipayClient(AlipayConfig.URL, AlipayConfig.APPID,
				AlipayConfig.RSA_PRIVATE_KEY, AlipayConfig.FORMAT, AlipayConfig.CHARSET, AlipayConfig.ALIPAY_PUBLIC_KEY,
				AlipayConfig.SIGNTYPE);
		
		// 调用手机支付实体类
		// AlipayTradeWapPayRequest alipay_request=new AlipayTradeWapPayRequest();
		
		// 调用网站支付实体类
		AlipayTradePagePayRequest alipay_request = new AlipayTradePagePayRequest();//创建API对应的reque
		
		// 超时时间 可空
		String timeout_express = "2m";
		// 销售产品码 必填
		String product_code = "FAST_INSTANT_TRADE_PAY";

		// 封装请求支付信息
		AlipayTradeWapPayModel model = new AlipayTradeWapPayModel();
		model.setOutTradeNo("201791512136140");
		model.setSubject("Iphone6 16G");
		model.setTotalAmount("88.88");
		model.setBody("Iphone6 16G");
		model.setTimeoutExpress(timeout_express);
		model.setProductCode(product_code);
		alipay_request.setBizModel(model);

		// 设置异步通知地址
		alipay_request.setNotifyUrl(AlipayConfig.notify_url);
		// 设置同步地址
		alipay_request.setReturnUrl(AlipayConfig.return_url);

		// form表单生产
		String form = "";
		try {
			// 调用SDK生成表单
			form = client.pageExecute(alipay_request).getBody();
			System.out.println("form："+form);
		} catch (AlipayApiException e) {
			e.printStackTrace();
		}
	}
}
