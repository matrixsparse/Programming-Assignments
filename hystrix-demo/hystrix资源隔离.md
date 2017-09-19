
## hystrix资源隔离

### pom.xml

```bash
<dependency>
	<groupId>org.apache.httpcomponents</groupId>
	<artifactId>httpclient</artifactId>
	<version>4.4</version>
</dependency>
```

```bash
<dependency>
    <groupId>com.netflix.hystrix</groupId>
    <artifactId>hystrix-core</artifactId>
    <version>1.5.12</version>
</dependency>
```

### 将hystrix-cache-ha/商品服务接口调用的逻辑进行封装

```bash
hystrix进行资源隔离，其实是提供了一个抽象，叫做command，如果要把对某一个依赖服务的所有调用请求，全部隔离在同一份资源池内

对这个依赖服务的所有调用请求，全部走这个资源池内的资源，不会去用其他的资源了，这个就叫做资源隔离

hystrix线程池隔离技术 是最基本的资源隔离的技术

对某一个依赖服务，商品服务，所有的调用请求，全部隔离到一个线程池内，对商品服务的每次调用请求都封装在一个command里面

每个command（每次服务调用请求）都是使用线程池内的一个线程去执行的

所以哪怕是对这个依赖服务，商品服务，现在同时发起的调用量已经到了1000了，但是线程池内就10个线程，最多就只会用这10个线程去执行

不会说，对商品服务的请求，因为接口调用延迟，将tomcat内部所有的线程资源全部耗尽，不会出现了
```

### src/main/java/**/model/ProductInfo.java

```bash
package com.matrix.hystrix.ha.model;

/**
 * 商品信息
 */
public class ProductInfo {

    private Long id;
    private String name;
    private Double price;
    private String pictureList;
    private String specification;
    private String service;
    private String color;
    private String size;
    private Long shopId;
    private String modifiedTime;

    public ProductInfo() {

    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Double getPrice() {
        return price;
    }

    public String getPictureList() {
        return pictureList;
    }

    public String getSpecification() {
        return specification;
    }

    public String getService() {
        return service;
    }

    public String getColor() {
        return color;
    }

    public String getSize() {
        return size;
    }

    public Long getShopId() {
        return shopId;
    }

    public String getModifiedTime() {
        return modifiedTime;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public void setPictureList(String pictureList) {
        this.pictureList = pictureList;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public void setService(String service) {
        this.service = service;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public void setShopId(Long shopId) {
        this.shopId = shopId;
    }

    public void setModifiedTime(String modifiedTime) {
        this.modifiedTime = modifiedTime;
    }

    @Override
    public String toString() {
        return "ProductInfo [id=" + id + ", name=" + name + ", price=" + price
                + ", pictureList=" + pictureList + ", specification="
                + specification + ", service=" + service + ", color=" + color
                + ", size=" + size + ", shopId=" + shopId + ", modifiedTime="
                + modifiedTime + "]";
    }
}
```

### src/main/java/**/hystrix/GetProductInfoCommand.java

```bash
package com.matrix.hystrix.ha.hystrix;

import com.alibaba.fastjson.JSONObject;
import com.matrix.hystrix.ha.http.HttpClientUtils;
import com.matrix.hystrix.ha.model.ProductInfo;
import com.netflix.hystrix.HystrixCommand;
import com.netflix.hystrix.HystrixCommandGroupKey;

/**
 * 获取商品信息
 */
public class GetProductInfoCommand extends HystrixCommand<ProductInfo> {

    private Long productId;

    public GetProductInfoCommand(Long productId) {
        super(HystrixCommandGroupKey.Factory.asKey("GetProductInfoGroup"));
        this.productId = productId;
    }

    protected ProductInfo run() throws Exception {
        String url = "http://127.0.0.1:8082/getProductInfo?productId=" + productId;
        String response = HttpClientUtils.sendGetRequest(url);
        return JSONObject.parseObject(response, ProductInfo.class);
    }
}
```

### src/main/java/**/hystrix/GetProductInfoCommand.java

```bash
package com.matrix.hystrix.ha.hystrix;

import com.alibaba.fastjson.JSONObject;
import com.matrix.hystrix.ha.http.HttpClientUtils;
import com.matrix.hystrix.ha.model.ProductInfo;
import com.netflix.hystrix.HystrixCommandGroupKey;
import com.netflix.hystrix.HystrixObservableCommand;
import rx.Observable;
import rx.Subscriber;

/**
 * 批量查询多个商品数据的command
 */
public class GetProductInfosCommand extends HystrixObservableCommand<ProductInfo> {

    private String[] productIds;

    public GetProductInfosCommand(String[] productIds) {
        super(HystrixCommandGroupKey.Factory.asKey("GetProductInfoGroup"));
        this.productIds = productIds;
    }

    @Override
    public Observable<ProductInfo> construct() {
        return Observable.create(new Observable.OnSubscribe<ProductInfo>() {

            public void call(Subscriber<? super ProductInfo> observer) {
                try {
                    for (String productId : productIds) {
                        String url = "http://127.0.0.1:8082/getProductInfo?productId=" + productId;
                        String response = HttpClientUtils.sendGetRequest(url);
                        ProductInfo productInfo = JSONObject.parseObject(response, ProductInfo.class);
                        observer.onNext(productInfo);
                    }
                    observer.onCompleted();
                } catch (Exception e) {
                    observer.onError(e);
                }
            }
        });
    }
}
```

### src/main/java/**/HttpClientUtils.java

```bash
package com.matrix.hystrix.ha.http;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

/**
 * HttpClient工具类
 */
@SuppressWarnings("deprecation")
public class HttpClientUtils {
    /**
     * 发送GET请求
     *
     * @param url 请求URL
     * @return 响应结果
     */
    @SuppressWarnings("resource")
    public static String sendGetRequest(String url) {
        String httpResponse = null;

        HttpClient httpclient = null;
        InputStream is = null;
        BufferedReader br = null;

        try {
            // 发送GET请求
            httpclient = new DefaultHttpClient();
            HttpGet httpget = new HttpGet(url);
            HttpResponse response = httpclient.execute(httpget);

            // 处理响应
            HttpEntity entity = response.getEntity();
            if (entity != null) {
                is = entity.getContent();
                br = new BufferedReader(new InputStreamReader(is));

                StringBuffer buffer = new StringBuffer("");
                String line = null;

                while ((line = br.readLine()) != null) {
                    buffer.append(line + "\n");
                }

                httpResponse = buffer.toString();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (br != null) {
                    br.close();
                }
                if (is != null) {
                    is.close();
                }
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }

        return httpResponse;
    }

    /**
     * 发送post请求
     *
     * @param url URL
     * @param map 参数Map
     * @return
     */
    @SuppressWarnings({"rawtypes", "unchecked", "resource"})
    public static String sendPostRequest(String url, Map<String, String> map) {
        HttpClient httpClient = null;
        HttpPost httpPost = null;
        String result = null;

        try {
            httpClient = new DefaultHttpClient();
            httpPost = new HttpPost(url);

            //设置参数
            List<NameValuePair> list = new ArrayList<NameValuePair>();
            Iterator iterator = map.entrySet().iterator();
            while (iterator.hasNext()) {
                Entry<String, String> elem = (Entry<String, String>) iterator.next();
                list.add(new BasicNameValuePair(elem.getKey(), elem.getValue()));
            }
            if (list.size() > 0) {
                UrlEncodedFormEntity entity = new UrlEncodedFormEntity(list, "utf-8");
                httpPost.setEntity(entity);
            }

            HttpResponse response = httpClient.execute(httpPost);
            if (response != null) {
                HttpEntity resEntity = response.getEntity();
                if (resEntity != null) {
                    result = EntityUtils.toString(resEntity, "utf-8");
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {

        }

        return result;
    }
}
```

### src/main/java/**/CacheController.java

```bash
package com.matrix.hystrix.ha.controller;

import com.matrix.hystrix.ha.http.HttpClientUtils;
import com.matrix.hystrix.ha.hystrix.GetProductInfoCommand;
import com.matrix.hystrix.ha.hystrix.GetProductInfosCommand;
import com.matrix.hystrix.ha.model.ProductInfo;
import com.netflix.hystrix.Hystrix;
import com.netflix.hystrix.HystrixCommand;
import com.netflix.hystrix.HystrixObservableCommand;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import rx.Observable;
import rx.Observer;

/**
 * 缓存服务的接口
 */
@Controller
public class CacheController {

    @RequestMapping("/change/product")
    @ResponseBody
    public String changeProduct(Long productId) {
        // 拿到一个商品id
        // 调用商品服务的接口，获取商品id对应的商品的最新数据
        // 用HttpClient去调用商品服务的http接口

        // 往http接口发送一条消息，就认为是通知缓存服务，有一个商品的数据变更了
        String url = "http://127.0.0.1:8082/getProductInfo?productId=" + productId;
        String response = HttpClientUtils.sendGetRequest(url);
        System.out.println(response);

        return "success";
    }

    /**
     * nginx开始，各级缓存都失效了，nginx发送很多的请求直接到缓存服务要求拉取最原始的数据
     */
    @RequestMapping("/getProductInfo")
    @ResponseBody
    public String getProductInfo(Long productId) {
        // 拿到一个商品id
        // 调用商品服务的接口，获取商品id对应的商品的最新数据
        // 用HttpClient去调用商品服务的http接口
        HystrixCommand<ProductInfo> getProductInfoCommand = new GetProductInfoCommand(productId);
        ProductInfo productInfo = getProductInfoCommand.execute();

        System.out.println(productInfo);
        return "success";
    }

    /**
     * 一次性批量查询多条商品数据的请求
     */
    @RequestMapping("/getProductInfos")
    @ResponseBody
    public String getProductInfos(String productIds) {
        HystrixObservableCommand<ProductInfo> getProductInfosCommand =
                new GetProductInfosCommand(productIds.split(","));
        Observable<ProductInfo> observable = getProductInfosCommand.observe();

//		observable = getProductInfosCommand.toObservable(); // 还没有执行

        observable.subscribe(new Observer<ProductInfo>() { // 等到调用subscribe然后才会执行

            public void onCompleted() {
                System.out.println("获取完了所有的商品数据");
            }

            public void onError(Throwable e) {
                e.printStackTrace();
            }

            public void onNext(ProductInfo productInfo) {
                System.out.println(productInfo);
            }

        });
        return "success";
    }
}
```