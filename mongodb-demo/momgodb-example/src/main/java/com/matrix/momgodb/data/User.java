package com.matrix.momgodb.data;

import java.io.Serializable;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import lombok.Data;

@Data
@Document(collection = "user") // 这个POJO最终要持久化为MongoDB中的document
public class User implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@Field("id")
	private int id;

	@Field("name")
	private String name;

	@Field("address")
	private String address;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

}
