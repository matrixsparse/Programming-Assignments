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
