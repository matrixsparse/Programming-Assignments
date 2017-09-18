
## hystrix资源隔离

### pom.xml

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